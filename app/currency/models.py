from django.db import models



# Create your models here.
class Currency(models.Model):
    Name = models.CharField(max_length=100)
    Amount = models.DecimalField(decimal_places=10, max_digits=100)
    def __str__(self):
        return self.Name
