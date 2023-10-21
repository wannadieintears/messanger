from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    ...
    phone = models.BigIntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    ...
    REQUIRED_FIELDS = ['email', 'age', 'phone']

