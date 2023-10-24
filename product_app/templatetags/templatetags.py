from django import template

from product_app.models import Product

register = template.Library()


@register.filter
def get_list(dictionary, key):
    return dictionary.getlist(key)


@register.filter
def category_len(title):
    cat_len = Product.objects.filter(category__title=title).count()
    return cat_len
