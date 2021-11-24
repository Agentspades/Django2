from django.urls import path, include
from rest_framework import routers

from .views import Booking, BookingsViewSet, UpdateBooking

router = routers.DefaultRouter()
router.register('bookings', BookingsViewSet, basename='bookings')

urlpatterns = [
    path('restaurant/book/', Booking.as_view()),
    path('restaurant/booking/update/', UpdateBooking.as_view()),
    path('restaurant/', include(router.urls)),
]
