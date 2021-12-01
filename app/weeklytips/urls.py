from django.urls import path, include
from rest_framework.routers import DefaultRouter
from weeklytips.models import SustainableTips

from weeklytips import views

router = DefaultRouter()
router.register('profile', views.TipsViewSet, basename="get_tip")

urlpatterns = [
    path('tips/', views.PostTips.as_view()),
    path('tips/', include(router.urls))
]
