from django.urls import path
from . import views


app_name = "product_app"
urlpatterns = [
    path("detail/<str:slug>", views.product_detail, name="detail"),
    path("add_review/<int:pk>", views.add_comment, name="add_review"),
    path("search_products", views.search, name="search"),
    path("store", views.store, name="store"),
    path("order_ajax/<str:pk>/<int:page>", views.store_order_ajax, name="store_ajax"),
    path("order_ajax2/<str:pk>/<int:page>", views.store_ajax2, name="store_order_ajax2"),
]
