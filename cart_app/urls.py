from django.urls import path
from . import views

app_name = "cart_app"
urlpatterns = [
    path("cart_add/<int:pk>/", views.cart_add, name="add"),
    path("cart_add_store/<int:pk>/", views.cart_add_store, name="cart_add_store"),
    path("remove_from_cart/<int:pk>/", views.remove_from_cart, name="remove_cart"),
    path("cart_list", views.cart_page, name="cart_list"),
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
