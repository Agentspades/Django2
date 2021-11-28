from rest_framework import serializers
from .models import RestaurantBooking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantBooking
        fields = '__all__'


class Booking(serializers.Serializer):
    phone = serializers.IntegerField()
    guests = serializers.IntegerField()
    datetime = serializers.DateTimeField()
