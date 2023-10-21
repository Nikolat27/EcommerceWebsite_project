from django.db import models

from account_app.models import User
from product_app.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_price = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.phone


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    color = models.CharField(max_length=30)
    quantity = models.IntegerField(default=1)
    price = models.PositiveIntegerField()

    @property
    def costprice(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.order.user.username} - {self.product.title}"


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    full_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    city = models.CharField(max_length=40, null=True, blank=True)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.user.phone
