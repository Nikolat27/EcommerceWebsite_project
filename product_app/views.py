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
    paginator = Paginator(products, 4)
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


def store_ajax2(request, pk, page):
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


def post_like(request, slug, pk):
    product = Product.objects.get(id=pk)
    print("Anonymous user liked")
    ip = get_ip(request)
    if not IpModel.objects.filter(ip=ip):  # Add ip to the database
        IpModel.objects.create(ip=ip)
    if product.likee.filter(id=IpModel.objects.get(ip=ip).id).exists():
        product.likee.remove(IpModel.objects.get(ip=ip))
        return JsonResponse({"response": "unliked"})
    else:
        product.likee.add(IpModel.objects.get(ip=ip))
        return JsonResponse({"response": "liked"})


def home(request):
    items = NameSpace.objects.all()[:10]
    return render(request, 'product_app/test1.html', {'items': items})


def test2(request):
    for x in range(100):
        name = "Hello World!"
        NameSpace.objects.create(title=name)


def load_more(request):
    page = request.GET.get('page')
    items = NameSpace.objects.all()[page * 10:(page * 10) + 10]  # Fetch the next 10 items
    return JsonResponse({'data': render_to_string('product_app/item_list.html', {'items': items})})
