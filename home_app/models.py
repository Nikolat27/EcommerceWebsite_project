from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from account_app.models import User
from product_app.models import Product


# Create your models here.

class Banner(models.Model):
    picture = models.ImageField(upload_to="banner_slider/", width_field=2160, height_field=972)
    title = models.CharField(max_length=40)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="banner")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SliderProducts(models.Model):
    product = models.ManyToManyField(Product, related_name="slider_products")
    created_at = models.DateTimeField(auto_now_add=True)


class AboutUs(models.Model):
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"About Us"


class Ticket(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_tickets")
    title = models.CharField(max_length=40)
    ticket = models.TextField()
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.title}"
