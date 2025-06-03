# app/views.py
from django.http import JsonResponse
from .models import UserMessage

def save_message(request):
    user_id = 123456  # yoki requestdan oling
    message = "Salom, Django!"

    UserMessage(user_id=user_id, message=message).save()
    return JsonResponse({"status": "success"})
