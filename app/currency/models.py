from django.db import models



# Create your models here.
class Currency(models.Model):
    Name = models.CharField(max_length=100)
    sale_orders = models.TextField(null=True)
    buy_orders = models.TextField(null=True)
    sale_price = models.DecimalField(max_digits=1000, decimal_places=10, null=True)
    buy_price = models.DecimalField(max_digits=1000, decimal_places=10, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=10, null=True)
    def __str__(self):
        return self.Name
