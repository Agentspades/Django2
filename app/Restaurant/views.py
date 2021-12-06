from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Auth.models import User

from .serializers import Booking, BookingSerializer, Update
from .models import RestaurantBooking

# Create your views here.


class UpdateBooking(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = Update

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user
            guests = serializer.validated_data.get('guests')
            date = serializer.validated_data.get('datetime')
            try:
                registration = RestaurantBooking.objects.get(userID=user)
                registration.guests = guests
                registration.datetime = date
                registration.save()
                message = f'A record was updated for name: {user.name}, guests: {guests}, Date: {date}'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except:
                message = f'There was an error updating name: {user}, guests: {guests}, Date: {date}'
                return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Booking(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = Booking

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user
            phone = serializer.validated_data.get('phone')
            guests = serializer.validated_data.get('guests')
            date = serializer.validated_data.get('datetime')
            try:
                if RestaurantBooking.objects.filter(userID=user):
                    return Response({'message': f'User {user.name} already has a booking'}, status=status.HTTP_403_FORBIDDEN)
                new_record = RestaurantBooking(
                    userID=user, phone=phone, guests=guests, datetime=date)
                new_record.save()
                message = f'A booking was added for name: {user.name}, phone: {phone}, guests: {guests}, Date: {date}'
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
