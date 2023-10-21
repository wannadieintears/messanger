from django.db import models
from account.models import Account


class Chat(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    members = models.ManyToManyField(Account, symmetrical=True)