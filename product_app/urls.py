from django.urls import path
from . import views

app_name = "product_app"
urlpatterns = [
    path("detail/<str:slug>", views.product_detail, name="detail"),
    path("add_review/<int:pk>", views.add_comment, name="add_review"),
    path("del_review/<int:pk>", views.del_comments, name="del_review"),
    path("store", views.store, name="store"),
    path("user_comments", views.user_comments, name="user_comments"),
    path("like/<str:slug>/<int:pk>/", views.like, name="like"),
    path("un_like/<str:slug>", views.un_like, name="unlike"),
    path("wishlist", views.wishlist, name="wishlist"),

]
