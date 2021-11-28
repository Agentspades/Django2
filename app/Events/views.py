from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from Auth.models import User

from .serializers import RegistrationList, RegistrationSerializer, EventList, UpdateSerializer
from .models import EventRegistration, Event


def GetUser(request):
    return request.user


@api_view(('GET', ))
def eventView(request, id):
    try:
        event = Event.objects.get(id=id)
        return Response({'detail': EventList(event).data})
    except:
        return Response({'Result': f'event {id} not found!'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateRegistration(APIView):
    serializer_class = UpdateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            event = serializer.validated_data.get('event')
            attendees = serializer.validated_data.get('attendees')
            try:
                userID = User.objects.get(email=email)
                user = EventRegistration.objects.get(
                    userID=userID, eventID=event)
                user.attendees = attendees
                user.save()
                message = f'A record was updated for user: {user}, email: {email}, attendees: {attendees}'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except:
                message = f'There was an error updating a user'
                return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Register(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user
            event = serializer.validated_data.get('event')
            attendees = serializer.validated_data.get('attendees')
            try:
                eventID = Event.objects.get(id=event)
                new_record = EventRegistration(
                    eventID=eventID, userID=user, attendees=attendees)
                new_record.save()
                message = f'A new record was added, user: {user}, event: {event}, attendees: {attendees}'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except:
                message = f'There was an error creating a registration'
                return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

####################### ViewSets ############################


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = RegistrationList
    http_method_names = ['get']


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventList
    http_method_names = ['get']
