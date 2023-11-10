from django.urls import path
from . import views


app_name = "home_app"
urlpatterns = [
    path("", views.home_app, name="main"),
    path("about_us", views.about_us, name="about_us"),
    path("contact_us", views.contact_us, name="contant_us"),
]
