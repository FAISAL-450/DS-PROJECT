# azure_auth/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.azure_login, name="azure_login"),
]

