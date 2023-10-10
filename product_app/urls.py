from django.urls import path
from . import views


app_name = "product_app"
urlpatterns = [
    path("detail/<str:slug>", views.product_detail, name="detail"),
    path("add_review/<int:pk>", views.add_comment, name="add_review"),
]
