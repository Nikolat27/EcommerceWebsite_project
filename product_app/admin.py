from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', "show_image"]


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ['title', 'show_image', 'parent']
    list_filter = ['parent']


admin.site.register(models.Color)
admin.site.register(models.Comment)
admin.site.register(models.Like)
