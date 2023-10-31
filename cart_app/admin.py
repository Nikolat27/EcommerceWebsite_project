from django.contrib import admin

from cart_app import models


# Register your models here.
class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "is_paid")
    inlines = (OrderItemAdmin,)
    search_fields = ("user__phone", "user__username", "order_number")
    list_filter = ("is_paid",)


admin.site.register(models.OrderItem)
