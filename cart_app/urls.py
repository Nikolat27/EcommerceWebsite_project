from django.urls import path
from . import views


app_name = "cart_app"
urlpatterns = [
    path("cart_add/<int:pk>/", views.cart_add, name="add"),
    path("cart_delete/<str:pk>/", views.delete_product, name="delete_product"),
    path("cart_list", views.cart_list, name="cart_list"),
    path("cart_list_del/<str:pk>", views.delete_cart_list, name="cart_list_del"),
    path("cart_update/<int:pk>", views.cart_update, name="cart_update"),
]
