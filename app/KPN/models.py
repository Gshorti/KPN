from django.db import models

from currency.models import Currency
from foreman.models import Foreman


# Create your models here.


class User(models.Model):
    Telegram_hash = models.CharField(max_length=100, null=False)
    Telegram_ID = models.CharField(max_length=100, null=True)
    Rubles = models.DecimalField(decimal_places=100, max_digits=1000, default=0)
    KPCS = models.DecimalField(decimal_places=100, max_digits=1000, default=0)
    Password = models.CharField(max_length=100)
    opened = models.TextField(null=True)
    history = models.TextField(null=True)
    avatar = models.FileField(upload_to="users",null=True)

    def __str__(self):
        return self.Telegram_hash


