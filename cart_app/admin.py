from django.contrib import admin

from cart_app import models


# Register your models here.

class CartItemTabularInLine(admin.TabularInline):
    model = models.CartItem


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemTabularInLine]


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "is_paid", "created_at")
    inlines = (OrderItemAdmin,)
    search_fields = ("user__phone", "user__username", "order_number")
    list_filter = ("is_paid",)


admin.site.register(models.OrderItem)
admin.site.register(models.Address)
