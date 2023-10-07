from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', "show_image"]


admin.site.register(models.Category)
admin.site.register(models.Color)
