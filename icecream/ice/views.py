from django.http import JsonResponse
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_message(request):
    print("Request method:", request.method)  # Debug print
    print("Request POST data:", dict(request.POST))  # Debug print

    if request.method == 'POST':
        message = request.POST.get('message')
        if not message:
            return JsonResponse({'error': 'Please enter a message.'}, status=400)
        
        # Send message to Telegram
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
            'text': message
        }
        try:
            response = requests.post(url, data=payload)
            print("Telegram response status:", response.status_code)  # Debug print
            print("Telegram response text:", response.text)  # Debug print
            if response.status_code == 200:
                return JsonResponse({'success': 'Message sent successfully!'})
            else:
                return JsonResponse({'error': f'Failed to send message to Telegram. Status: {response.status_code}'}, status=500)
        except requests.RequestException as e:
            print("Telegram request exception:", str(e))  # Debug print
            return JsonResponse({'error': 'Error connecting to Telegram.'}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)