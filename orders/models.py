from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.BigIntegerField()
    customer_id = models.BigIntegerField()
    shipping = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField()

class OrderItem(models.Model):
    order_id = models.BigIntegerField()
    product_name = models.CharField(max_length=100)
    qty = models.PositiveIntegerField()