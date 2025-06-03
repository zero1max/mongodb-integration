# app/models.py
from mongoengine import Document, StringField, IntField

class UserMessage(Document):
    user_id = IntField(required=True)
    message = StringField(required=True)
