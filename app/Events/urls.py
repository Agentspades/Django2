from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from Events import views

router = routers.DefaultRouter()  # creates a router
router.register('registrations',
                views.RegistrationViewSet, basename='registrations')
router.register('all', views.EventViewSet, basename='events')

urlpatterns = [
    path('events/register/', views.Register.as_view()),
    path('registration/update/', views.UpdateRegistration.as_view()),
    url('events/registrations/(?P<id>\d+)/', views.eventView,),
    url('events/check/(?P<id>\d+)/', views.checkAttendees,),
    path('events/', include(router.urls)),
]
