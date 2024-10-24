# myapp/urls.py
from django.urls import path
from .views import send_message_view, receive_messages_view

urlpatterns = [
    path('send-message/', send_message_view, name='send_message'),
    path('receive-messages/', receive_messages_view, name='receive_messages'),
]
