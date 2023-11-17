from django.urls import path
from . import views


app_name = "cart_app"
urlpatterns = [
    path("cart_add/<int:pk>/", views.cart_add, name="add"),
    path("cart_add_store/<int:pk>/", views.cart_add_store, name="cart_add_store"),
    path("cart_delete/<str:pk>/", views.delete_product, name="delete_product"),
    path("cart_delete_base/<str:pk>/", views.delete_product_base, name="delete_product_base"),
    path("cart_list", views.cart_list, name="cart_list"),
    path("cart_list_del/<str:pk>", views.delete_cart_list, name="cart_list_del"),
    path("cart_update/<int:pk>", views.cart_update, name="cart_update"),
    path("checkout", views.checkout, name="checkout"),
    path("order_creation", views.order_creation, name="order_creation"),
    path("order_detail/<int:pk>", views.order_detail, name="order_detail"),
    path("factor_page/<int:pk>", views.view_factor, name="factor_page"),
    path("purchases", views.purchases, name="purchases"),
    path("address", views.address, name="address"),
    path("edit_address/<int:pk>", views.edit_address, name="edit_address"),
    path("test", views.test1),
]
