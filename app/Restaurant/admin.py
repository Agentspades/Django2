from django.contrib import admin
from .models import RestaurantBooking


class RestaurantBookingsAdmin(admin.ModelAdmin):
    search_fields = ['Ppone']


# Register your models here.
admin.site.register(RestaurantBooking, RestaurantBookingsAdmin)
