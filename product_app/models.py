from django.db import models
from django.db.models import Model
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
# Create your models here.


class Category(Model):
    title = models.CharField(max_length=30, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="subs", null=True, blank=True)

    def __str__(self):
        return self.title


class Color(Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class Product(Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="img/product-pics", null=True, blank=True)
    color = models.ManyToManyField(Color, related_name="colors")
    price = models.IntegerField()
    category = models.ManyToManyField(Category, related_name="categories")
    quantity = models.SmallIntegerField()
    discount = models.SmallIntegerField(null=True, blank=True, default=0, help_text="if u dont want to discount a price,"
                                                                         " dont touch this field Tnx :)")
    available = models.BooleanField()
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save()

    def discount_price(self):
        if self.discount != 0:
            discount_price = self.price * self.discount // 100
            total_price = self.price - discount_price

            return total_price

    def get_absolute_url(self):
        return reverse("product_app:detail", kwargs={"slug": self.slug})

    def show_image(self):
        if self.image:
            return format_html(f"<img src='{self.image.url}' width='70px' height='70px'>")
        else:
            return format_html(f"<img src='sdfasdf' alt='No Image Available' >")
