from django.db import models

from currency.models import Currency
from foreman.models import Foreman


# Create your models here.


class User(models.Model):
    Telegram_hash = models.CharField(max_length=100)
    Telegram_ID = models.CharField(max_length=100)
    Rubles = models.DecimalField(decimal_places=100, max_digits=1000)
    KPCS = models.DecimalField(decimal_places=100, max_digits=1000)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Telegram_hash


