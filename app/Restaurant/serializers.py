from django.core import validators
from rest_framework import serializers
from .models import RestaurantBooking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantBooking
        fields = '__all__'


class Booking(serializers.Serializer):
    phone = serializers.IntegerField()
    guests = serializers.IntegerField(min_value=1, max_value=10)
    datetime = serializers.DateTimeField()


class Update(serializers.Serializer):
    guests = serializers.IntegerField(min_value=1, max_value=10)
    datetime = serializers.DateTimeField()
