from django.db.models import Max, Min, Avg
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from weblog_app.models import IpModel
from weblog_app.views import get_ip
from .models import Product, Color, Review, Category, Like, NameSpace


# Create your views here.


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.user.is_authenticated and request.user.likes.filter(product__slug=product.slug,
                                                                   user=request.user).exists():
        is_liked = True
    else:
        is_liked = False
    # related_products = Product.objects.filter(category__title=product.category.first().title)[:8]
    related_products = Product.objects.filter(category__in=product.category.all()).distinct()
    return render(request, "product_app/product_detail.html",
                  context={"product": product, "related_products": related_products, "is_liked": is_liked})


@login_required
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
            comment = Review.objects.create(name=name, body=body, product=product, pros=pros,
                                            cons=cons, author=author, rating=rating, parent_id=parent_id)
            return render(request, "product_app/product_detail.html", context={"product": product, "related_product":
                related_products})
        else:
            parent_id = None
            comment = Review.objects.create(name=name, body=body, product=product, pros=pros,
                                            cons=cons, author=author, rating=rating)
            return render(request, "product_app/product_detail.html", context={"product": product, "related_product":
                related_products})


@login_required
def del_comments(request, pk):
    del_comment = Review.objects.get(author=request.user, id=pk)
    del_comment.delete()
    del_comment.save()

    return redirect("product_app:user_comments")


def store(request):
    categories = request.GET.getlist("category")
    page = request.GET.get("page")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    colors = request.GET.getlist("color")
    q = request.GET.get("q")
    sort = request.GET.get("sort", "default")

    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']

    if 'sort' in query_params:
        del query_params['sort']

    if "min_price" in query_params:
        del query_params['min_price']

    if "max_price" in query_params:
        del query_params['max_price']

    products_count = Product.objects.all().count()

    products = Product.objects.all().order_by("-created_at").distinct()
    if q:
        products = products.filter(title__icontains=q)

    if categories:
        products = products.filter(category__title__in=categories)

    if min_price and max_price:
        products = products.filter(price__range=(min_price, max_price))

    if colors:
        products = products.filter(color__title__in=colors)

    if sort == "popular":
        products = products.annotate(avg_rating=Avg('comments__rating')).order_by('-avg_rating')
    elif sort == "most_sold":
        products = products.order_by("sold")
    elif sort == "new":
        products = products.order_by("-created_at")
    elif sort == "cheapest":
        products = products.order_by("price")
    elif sort == "most_expensive":
        products = products.order_by("-price")

    nonsub_categories = Category.objects.filter(parent=None)  # non subcategories Categories
    max_price = products.aggregate(Max('price'))['price__max']
    min_price = products.aggregate(Min('price'))['price__min']
    paginator = Paginator(products, 1)
    products = paginator.get_page(page)

    return render(request, "product_app/store.html", context={"products": products, "products_count": products_count,
                                                              "nonsub_categories": nonsub_categories,
                                                              "query_params": query_params.urlencode(),
                                                              "max_price": max_price, "min_price": min_price})


@login_required
def user_comments(request):
    comments = Review.objects.filter(author=request.user)
    return render(request, "product_app/user_comments.html", context={"comments": comments})


@login_required
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


@login_required
def un_like(request, slug):
    like = Like.objects.get(product__slug=slug, user=request.user)
    like.delete()
    return redirect("product_app:wishlist")


@login_required
def wishlist(request):
    wishlist = Product.objects.filter(likes__user=request.user)
    return render(request, "product_app/wishlist.html", context={"wishlist": wishlist, "wishlist_len": len(wishlist)})


def home(request):
    items = NameSpace.objects.all()[:10]
    return render(request, 'product_app/test1.html', {'items': items})
