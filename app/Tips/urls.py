from django.urls import path
from .views import NewTip, GetTip

urlpatterns = [
    path('tip/new/', NewTip),
    path('tip/get/', GetTip),
]
