from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():

    SECRET_TOKEN = 'your_github_webhook_secret_token'

    # Verify the GitHub webhook signature
    signature = request.headers.get('X-Hub-Signature')
    if signature is None:
        return jsonify({'error': 'Missing signature'}), 400

    sha1, sent_signature = signature.split('=')
    mac = hmac.new(SECRET_TOKEN.encode(), request.data, hashlib.sha1)
    if not hmac.compare_digest(mac.hexdigest(), sent_signature):
        return jsonify({'error': 'Invalid signature'}), 400

    # Process the webhook payload
    payload = request.json
    event_type = request.headers.get('X-GitHub-Event')
    print(f"Event received: {event_type}, Payload: {payload}")
    
    # You can trigger your deployment or any other action here
    
    return jsonify({'status': 'success'}), 200
