from django.urls import path
from . import views


app_name = "product_app"
urlpatterns = [
    path("detail/<str:slug>", views.product_detail, name="detail"),
    path("add_review/<int:pk>", views.add_comment, name="add_review"),
    path("del_review/<int:pk>", views.del_comments, name="del_review"),
    path("search_products", views.search, name="search"),
    path("store", views.store, name="store"),
    path("order_ajax/<str:pk>/<int:page>", views.store_order_ajax, name="store_ajax"),
    path("order_ajax2/<str:pk>/<int:page>", views.store_ajax2, name="store_order_ajax2"),
    path("user_comments", views.user_comments, name="user_comments"),
    path("like/<str:slug>/<int:pk>", views.like, name="like"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("un_like/<str:slug>", views.un_like, name="unlike"),
    path("post_like/<int:pk>", views.post_like, name="post_like"),
]
