from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.SliderProducts)
class SliderProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ("product",)


admin.site.register(models.Banner)
admin.site.register(models.AboutUs)
admin.site.register(models.Ticket)
