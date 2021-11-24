from django.contrib import admin
from django.urls import path
from .views import login, create

urlpatterns = [
    path('user/login/', login),
    path('user/create/', create),
]
