from django.http import JsonResponse
import hmac
import hashlib
from django.views.decorators.csrf import csrf_exempt

SECRET_TOKEN = 'your_github_webhook_secret_token'

@csrf_exempt  # Exempt CSRF validation for webhook calls
def handle_webhook(request):
    # Verify that the request is a POST
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method, only POST allowed'}, status=405)

    # Verify the GitHub webhook signature
    signature = request.headers.get('X-Hub-Signature')
    if signature is None:
        return JsonResponse({'error': 'Missing signature'}, status=400)

    sha1, sent_signature = signature.split('=')
    mac = hmac.new(SECRET_TOKEN.encode(), request.body, hashlib.sha1)
    if not hmac.compare_digest(mac.hexdigest(), sent_signature):
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    # Process the webhook payload
    payload = request.json()
    event_type = request.headers.get('X-GitHub-Event')
    print(f"Event received: {event_type}, Payload: {payload}")

    # Trigger your deployment or other actions here
    
    return JsonResponse({'status': 'success'}, status=200)
