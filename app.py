from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

sqs = boto3.client('sqs', region_name='your-region')
queue_url = os.environ.get('SQS_QUEUE_URL')

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    sqs.send_message(QueueUrl=queue_url, MessageBody=data['message'])
    return jsonify({'status': 'Message sent to queue'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
