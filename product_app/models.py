from django.db import models
from django.db.models import Model, Avg, Count
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
from account_app.models import User
from weblog_app.models import IpModel


# Create your models here.


class Category(Model):
    title = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to="category_pics", null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="subs", null=True, blank=True)

    def __str__(self):
        return self.title

    def show_image(self):
        if self.image:
            return format_html(f"<img src='{self.image.url}' width='70px' height='70px'>")
        else:
            return format_html(f"<img src='sdfasdf' alt='No Image Available' >")


class Color(Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class Product(Model):
    title = models.CharField(max_length=65, unique=True)
    english_title = models.CharField(max_length=65, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="img/product-pics")
    color = models.ManyToManyField(Color, related_name="colors")
    price = models.FloatField()
    category = models.ManyToManyField(Category, related_name="categories")
    quantity = models.SmallIntegerField()
    discount_percentage = models.SmallIntegerField(default=0,
                                                   help_text="if u dont want to discount a price,"
                                                             " dont touch this field Tnx :)")
    is_discounted = models.BooleanField(default=False)
    available = models.BooleanField()
    sold = models.PositiveBigIntegerField(default=0, editable=False)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save()

    def average_review(self):
        review = Review.objects.filter(product=self).aggregate(reviews=Avg('rating'))
        avg = 0
        if review["reviews"] is not None:
            avg = float(review["reviews"])
        return avg

    def len_average_review(self):
        review_len = Review.objects.filter(product=self)
        x = len(review_len)
        return x

    def discounted_price(self):
        if self.discount_percentage and self.discount_percentage > 0:
            discounted_price = (self.discount_percentage / 100) * self.price
            price = self.price - discounted_price
            return price
        else:
            return self.price

    def just_discount_price(self):
        if self.discount_percentage and self.discount_percentage > 0:
            discount_price = (self.discount_percentage / 100) * self.price
            return discount_price
        else:
            return 0

    def get_absolute_url(self):
        return reverse("product_app:detail", kwargs={"slug": self.slug})

    def show_image(self):
        if self.image:
            return format_html(f"<img src='{self.image.url}' width='70px' height='70px'>")
        else:
            return format_html(f"<img src='' alt='No Image Available' >")


class ProductDetail(Model):
    product = models.ForeignKey(Product, related_name="product_details", on_delete=models.CASCADE)
    question = models.CharField(max_length=50, null=True, blank=True)
    answer = models.CharField(max_length=50, null=True, blank=True)
    property = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.question} - {self.answer}"


class Review(Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
    pros = models.CharField(max_length=100, null=True, blank=True)
    cons = models.CharField(max_length=100, null=True, blank=True)
    CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rating = models.IntegerField(choices=CHOICES, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.author}"


class Like(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.phone} - {self.product.title}"


class NameSpace(Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
