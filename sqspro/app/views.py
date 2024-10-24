# myapp/views.py
from django.http import JsonResponse
from .sqs_utils import send_message_to_sqs, receive_messages_from_sqs

def send_message_view(request):
    message = "SQS Message."
    response = send_message_to_sqs(message)
    return JsonResponse({'status': 'Message sent', 'response': response})

def receive_messages_view(request):
    messages = receive_messages_from_sqs()
    return JsonResponse({'status': 'Messages received', 'messages': messages})
