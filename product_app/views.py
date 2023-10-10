from django.shortcuts import render, get_object_or_404
from .models import Product, Color, Comment


# Create your views here.


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # related_products = Product.objects.filter(category__title=product.category.first().title)[:8]
    related_products = Product.objects.filter(category__in=product.category.all()).distinct()
    return render(request, "product_app/product_detail.html",
                  context={"product": product, "related_products": related_products})


def add_comment(request, pk):
    if request.method == "POST":
        name = request.POST.get("f_name")
        body = request.POST.get("body")
        product = Product.objects.get(id=pk)
        pros = request.POST.get("pros")
        cons = request.POST.get("cons")
        author = request.user
        rating = request.POST.get("rating")
        parent_id = request.POST.get("parent_id")
        related_products = Product.objects.filter(category__in=product.category.all()).distinct()
        if parent_id:
            comment = Comment.objects.create(name=name, body=body, product=product, pros=pros,
                                             cons=cons, author=author, rating=rating, parent_id=parent_id)
            return render(request, "product_app/product_detail.html", context={"product": product, "related_product":
                                                                               related_products})
        else:
            parent_id = None
            comment = Comment.objects.create(name=name, body=body, product=product, pros=pros,
                                             cons=cons, author=author, rating=rating)
            return render(request, "product_app/product_detail.html", context={"product": product, "related_product":
                                                                               related_products})

