from django import template
from persiantools.jdatetime import JalaliDate

from cart_app.models import OrderItem
from product_app.models import Product

register = template.Library()


@register.filter
def get_list(dictionary, key):
    return dictionary.getlist(key)


@register.filter
def category_len(title):
    cat_len = Product.objects.filter(category__title=title).count()
    return cat_len


@register.filter
def jdate(date):
    new_date = JalaliDate.to_jalali(date)
    return new_date
