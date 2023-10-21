from django.db import models
from account.models import Account
from chats.models import Chat


class Message(models.Model):
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    where = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE)

