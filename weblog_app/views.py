from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from weblog_app.models import Weblog, WeblogComment, WeblogCategroy, IpModel, WeblogVideo, WeblogVideoComment


# Create your views here.
def blog(request):
    categories = WeblogCategroy.objects.all()
    popular_blogs = Weblog.objects.all().order_by("views")[:8]
    new_videos = WeblogVideo.objects.all().order_by("-created_at")[:8]
    latest = Weblog.objects.all().order_by("-created_at")[:8]
    return render(request, "weblog_app/blog.html", context={"categories": categories, "new_videos": new_videos, "latest"
    : latest, "popular_blogs": popular_blogs})


def blog_list(request):
    sort = request.GET.get("sort")
    blogs = Weblog.objects.all()
    if sort:
        if sort == "popular":
            # blogs = sorted(Weblog.objects.all(), key=lambda x: x.total_views())
            blogs = Weblog.objects.all().order_by("views").distinct()
        elif sort == "videos":
            blogs = WeblogVideo.objects.all().order_by("-created_at").distinct()
            print("hi 5 ")
        elif sort == "latest":
            blogs = Weblog.objects.all().order_by("-created_at").distinct()

    categories = WeblogCategroy.objects.all()
    page_number = request.GET.get("page")

    paginator = Paginator(blogs, 4)
    object_list = paginator.get_page(page_number)

    return render(request, "weblog_app/blog_list.html", context={"blogs": object_list, "categories": categories})


def get_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(",")[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def search_blogs(request):
    q = request.GET.get("search_blog")
    blogs = Weblog.objects.filter(main_title__icontains=q)
    categories = WeblogCategroy.objects.all()

    return render(request, "weblog_app/blog_list.html", context={"blogs": blogs, "categories": categories})


def blog_filter(request):
    categories1 = request.GET.getlist("category")
    page_number = request.GET.get("page")
    categories = WeblogCategroy.objects.all()
    blogs = Weblog.objects.filter(category__title__in=categories1)

    paginator = Paginator(blogs, 4)
    object_list = paginator.get_page(page_number)

    return render(request, "weblog_app/blog_list.html", context={"blogs": object_list, "categories": categories})


def blog_detail(request, slug):
    blog = Weblog.objects.get(slug=slug)
    related_blogs = Weblog.objects.filter(category__in=blog.category.all()).distinct()[:5]
    ip = get_ip(request)
    print(ip)
    if IpModel.objects.filter(ip=ip).exists():
        print("ip already exists")
        post = Weblog.objects.get(slug=slug)
        post.ip.add(IpModel.objects.get(ip=ip))
    else:
        IpModel.objects.create(ip=ip)
        post = Weblog.objects.get(slug=slug)
        post.ip.add(IpModel.objects.get(ip=ip))
    return render(request, "weblog_app/blog_detail.html", context={"blog": blog, "rb": related_blogs})


def blog_detail_video(request, slug):
    blog = WeblogVideo.objects.get(slug=slug)
    rb = WeblogVideo.objects.filter(category__in=blog.category.all())
    return render(request, "weblog_app/blog_detail_video.html", context={"blog": blog, "rb": rb})


def blog_comment(request, pk):
    if request.method == "POST":
        name = request.POST.get("name")
        body = request.POST.get("body")
        email = request.user.email
        parent_id = request.POST.get("parent_id")
        blog = Weblog.objects.get(id=pk)
        if parent_id:
            comment = WeblogComment.objects.create(name=name, body=body, email=email, author=request.user,
                                                   parent_id=parent_id, blog=blog)
        else:
            comment = WeblogComment.objects.create(name=name, body=body, email=email, author=request.user, blog=blog)
        return redirect("weblog_app:detail_blog", blog.slug)


def blog_video_comment(request, pk):
    if request.method == "POST":
        print(pk)
        name = request.POST.get("name")
        body = request.POST.get("body")
        email = request.user.email
        parent_id = request.POST.get("parent_id")
        blog = WeblogVideo.objects.get(id=pk)
        if parent_id:
            WeblogVideoComment.objects.create(name=name, body=body, email=email, author=request.user,
                                              parent_id=parent_id, blog=blog)
        else:
            WeblogVideoComment.objects.create(name=name, body=body, email=email, author=request.user,
                                              blog=blog)
        return redirect("weblog_app:blog_detail_video", blog.slug)
