from django.core import paginator
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.generic import DetailView

from .models import Product, Color, Comment, Category, Like


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


def search(request):
    q = request.GET.get("q")
    products = Product.objects.filter(title__istartswith=q)
    payload = []

    for product in products:
        payload.append({
            'title': product.title
        })
    return JsonResponse({'statues': True, 'payload': payload})


def store(request):  # This function is for filter the products in store page
    products = Product.objects.all()
    categories = request.GET.getlist("category")
    page_number = request.GET.get("page")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    colors = request.GET.getlist("color")
    q = request.GET.get("q")
    x = Product.objects.all().count()

    if q:
        products = Product.objects.filter(title__icontains=q)

    if categories:
        products = Product.objects.filter(category__title__in=categories)

    if min_price and max_price:
        products = Product.objects.filter(price__lte=max_price, price__gte=min_price)

    if colors:
        products = Product.objects.filter(color__title__in=colors)
    y = Category.objects.filter(parent=None)  # non subcategories Categories
    paginator = Paginator(products, 1)
    object_list = paginator.get_page(page_number)
    return render(request, "product_app/store.html", context={"products": object_list, "xq": x, "y": y})


def store_order_ajax(request, pk, page):  # This function is for order the products in store page with ajax

    products = Product.objects.all()
    if pk == "default":
        products = Product.objects.all()
    elif pk == "popular":
        products = Product.objects.filter(comments__rating__gt=4.5).distinct()
    elif pk == "newest":
        products = Product.objects.all().order_by("-created_at").distinct()
    elif pk == "cheap":
        products = Product.objects.all().order_by("-price").distinct()
    elif pk == "expensive":
        products = Product.objects.all().order_by("price").distinct()
    else:
        print("no pk!")

    if not page:
        page = 1

    paginator = Paginator(products, 1)
    object_list = paginator.get_page(page)
    data = render_to_string("AjaxTemplates/order_store_ajax.html", {"products": object_list, "pk": pk})
    if not data:
        print("no data")

    return JsonResponse({"bool": True, "data": data})


def store_ajax2(request, pk, page):  # This function is used for pagination because i couldnt do the
    # pagination with ajax and jsonresponse
    print("hello world")
    products = Product.objects.all()
    if pk == "default":
        products = Product.objects.all()
    elif pk == "popular":
        products = Product.objects.filter(comments__rating__gt=4.5).distinct()
    elif pk == "newest":
        products = Product.objects.all().order_by("-created_at").distinct()
    elif pk == "cheap":
        products = Product.objects.all().order_by("price").distinct()
    elif pk == "expensive":
        products = Product.objects.all().order_by("-price").distinct()
    else:
        print("no pk!")

    if not page:
        page = 1

    paginator = Paginator(products, 1)
    object_list = paginator.get_page(page)

    return render(request, "product_app/store2.html", {"products": object_list, "pk": pk})


def user_comments(request):
    if request.user.is_authenticated:
        comments = Comment.objects.filter(author=request.user)
        return render(request, "product_app/user_comments.html", context={"comments": comments})
    else:
        return redirect("home_app:main")


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_app/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.likes.filter(product__slug=self.object.slug,
                                                                                 user=self.request.user).exists():
            context["is_liked"] = True
        else:
            context["is_liked"] = False
        return context


def like(request, slug, pk):
    try:
        like = Like.objects.get(product__slug=slug, user=request.user)
        like.delete()
        liked_products = Product.objects.filter(likes__user=request.user)

        return JsonResponse({"response": "unliked", "likedproducts": len(liked_products)})
    except:
        Like.objects.create(product_id=pk, user_id=request.user.id)
        liked_products = Product.objects.filter(likes__user=request.user)
        return JsonResponse({"response": "liked", "likedproducts": len(liked_products)})
