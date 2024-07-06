from django.db import models

from currency.models import Currency
from foreman.models import Foreman


# Create your models here.


class User(models.Model):
    Telegram_hash = models.CharField(max_length=100)
    Telegram_ID = models.CharField(max_length=100)
    Rubles = models.IntegerField()
    KPСS = models.IntegerField()
    MONEYS = models.CharField(max_length=10000, default='0')
    MONEYTAP = models.CharField(max_length=10000, default='0')
    foreman = models.ManyToManyField(Foreman)
    is_foreman = models.BooleanField(default=False)

    def __str__(self):
        return self.Telegram_hash


