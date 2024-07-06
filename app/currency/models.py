from django.db import models



# Create your models here.
class Currency(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=10000)
    Rubles = models.FloatField(max_length=100000)
    KPNS = models.FloatField(max_length=100000)
    ratio = models.IntegerField(default=100)

    def __str__(self):
        return self.Name
