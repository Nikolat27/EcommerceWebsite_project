from django.urls import path
from . import views


app_name = "cart_app"
urlpatterns = [
    path("cart_add/<int:pk>", views.cart_add, name="add"),
    path("cart_delete/<str:pk>", views.delete_product, name="delete_product"),
]
