from . import views
from django.urls import path


app_name = "weblog_app"
urlpatterns = [
    path("detail/<str:slug>", views.blog_detail, name="detail_blog"),
    path("", views.blog, name="blog"),
    path("blog_comment/<int:pk>", views.blog_comment, name="blog_comments"),
    path("blog_list", views.blog_list, name="blog_list"),
    path("blog_search", views.search_blogs, name="blog_search"),
    path("blog_filter", views.blog_filter, name="blog_filter"),
    path("blog_video/<str:slug>", views.blog_detail_video, name="blog_detail_video"),
    path("video_comment/<int:pk>", views.blog_video_comment, name="blog_video_comment"),
]
