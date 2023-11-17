from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from weblog_app.models import Weblog
from .models import SliderProducts, AboutUs, Ticket
from product_app.models import Product, Category


# Create your views here.


def home_app(request):
    products = Product.objects.all()
    myproduct = SliderProducts.objects.get(id=3)
    slider_products = myproduct.product.all()[:4]
    latest_blogs = Weblog.objects.all()[:8]
    categories = Category.objects.filter(parent=None)[:8]
    return render(request, "home_app/index.html", context={"products": products, "slider_products": slider_products,
                                                           "latest_blogs": latest_blogs, "categories": categories})


def about_us(request):
    content = AboutUs.objects.get(id=1)
    return render(request, "home_app/about-us.html", context={"about_us": content})


@login_required
def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        body = request.POST.get("body")
        author = request.user
        title = request.POST.get("title")
        Ticket.objects.create(name=name, email=email, ticket=body, author=author, title=title)

        return redirect("home_app:contant_us")
    return render(request, "home_app/contact-us.html")
