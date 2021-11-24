from rest_framework.decorators import APIView, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from Auth.models import User

from .serializers import Booking, BookingSerializer
from .models import RestaurantBooking

# Create your views here.


class UpdateBooking(APIView):
    serializer_class = Booking

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            phone = serializer.validated_data.get('phone')
            guests = serializer.validated_data.get('guests')
            date = serializer.validated_data.get('datetime')
            try:
                user = User.objects.get(email=email)
                registration = RestaurantBooking.objects.get(userID=user)
                registration.guests = guests
                registration.datetime = date
                registration.save()
                message = f'A record was updated for name: {user}, phone: {phone}, guests: {guests}, Date: {date}'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except:
                message = f'There was an error updating name: {user}, phone: {phone}, guests: {guests}, Date: {date}'
                return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Booking(APIView):
    serializer_class = Booking

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            phone = serializer.validated_data.get('phone')
            guests = serializer.validated_data.get('guests')
            date = serializer.validated_data.get('datetime')
            try:
                user = User.objects.get(email=email)
                new_record = RestaurantBooking(
                    userID=user, phone=phone, guests=guests, datetime=date)
                new_record.save()
                message = f'A booking was added for name: {user}, phone: {phone}, guests: {guests}, Date: {date}'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except:
                message = f'There was an error saving the booking'
                return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

####################### ViewSets ############################


class BookingsViewSet(viewsets.ModelViewSet):
    queryset = RestaurantBooking.objects.all()
    serializer_class = BookingSerializer
    http_method_names = ['get']
