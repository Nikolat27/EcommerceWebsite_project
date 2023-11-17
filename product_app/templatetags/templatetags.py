from django import template
from persiantools.jdatetime import JalaliDate
from product_app.models import Product
from weblog_app.models import Weblog

register = template.Library()


@register.filter
def get_list(dictionary, key):
    return dictionary.getlist(key)


@register.filter
def category_len(title):
    cat_len = Product.objects.filter(category__title=title).count()
    return cat_len


@register.filter
def blog_category_len(title):
    cat_len = Weblog.objects.filter(category__title=title).count()
    return cat_len


@register.filter
def jdate(date):
    new_date = JalaliDate.to_jalali(date)
    shamsi_months = {1: "فروردین",
                     2: "اردیبهشت",
                     3: "خرداد",
                     4: "تیر",
                     5: "مرداد",
                     6: "شهریور",
                     7: "مهر",
                     8: "آبان",
                     9: "آذر",
                     10: "دی",
                     11: "بهمن",
                     12: "اسفند"}
    year = new_date.year
    month = new_date.month
    day = new_date.day

    for x in shamsi_months:
        if month == x:
            return f"{day} , {shamsi_months[month]} , {year}"


@register.filter
def jdate_year(date):
    new_date = JalaliDate.to_jalali(date)
    year = new_date.year
    return year


@register.filter
def is_liked(pk, request):
    product = Product.objects.get(id=pk)
    if request.user.is_authenticated and request.user.likes.filter(product__slug=product.slug,
                                                                   user=request.user).exists():
        return True
    else:
        return False


@register.filter
def slider_product(date):
    return f"{date.year}-{date.month}-{date.day}"
