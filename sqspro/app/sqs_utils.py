
import boto3
from django.conf import settings

# Initialize SQS client using credentials from Django settings
sqs_client = boto3.client('sqs', 
                          region_name=settings.AWS_REGION,
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

def send_message_to_sqs(message_body):
    try:
        response = sqs_client.send_message(
            QueueUrl=settings.SQS_QUEUE_URL,
            MessageBody=message_body,
        )
        return response
    except Exception as e:
        print(f"Error sending message to SQS: {e}")


def receive_messages_from_sqs():
    try:
        response = sqs_client.receive_message(
            QueueUrl=settings.SQS_QUEUE_URL,
            MaxNumberOfMessages=10,  
            WaitTimeSeconds=10,      
        )
        messages = response.get('Messages', [])
        # messages = response['Messages']
        return messages
        # return response
    except Exception as e:
        print(f"Error receiving messages from SQS: {e}")
        return []
