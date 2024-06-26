from django.contrib import admin
from . import models


# Register your models here.

class DetailAdmin(admin.TabularInline):
    model = models.ProductDetail


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (DetailAdmin,)
    search_fields = ("title",)
    list_display = ['title', 'price', "show_image"]


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ['title', 'show_image', 'parent']
    list_filter = ['parent']


admin.site.register(models.Color)
admin.site.register(models.Review)
admin.site.register(models.Like)
admin.site.register(models.NameSpace)
