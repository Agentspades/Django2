from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .serializers import RegistrationList, RegistrationSerializer, EventList
from .models import EventRegistration, Event


@api_view(('GET', ))
def checkAttendees(request, id):
    try:
        event = Event.objects.get(id=id)
        maxAttendees = event.maxAttendees
        currentlyBooked = EventRegistration.objects.filter(
            eventID=id).aggregate(Sum('attendees'))['attendees__sum']
        if currentlyBooked == None:
            currentlyBooked = 0
        spotsLeft = maxAttendees - currentlyBooked
        return Response({'remaining': spotsLeft}, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'error checking attendee count'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', ))
def eventView(request, id):
    try:
        event = Event.objects.get(id=id)
        return Response({'detail': EventList(event).data})
    except:
        return Response({'Result': f'event {id} not found!'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateRegistration(APIView):
    permission_classes = (IsAuthenticated)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user
            eventID = serializer.validated_data.get('event')
            event = Event.objects.filter(id=eventID)
            attendees = serializer.validated_data.get('attendees')
            count = EventRegistration.objects.filter(
                eventID=eventID).aggregate(Sum('attendees'))['attendees__sum']
            if count == None:
                count = 0
            try:
                userReg = EventRegistration.objects.filter(
                    userID=user, eventID=event)
                if ((count + attendees) <= event.maxAttendees):
                    userReg.attendees = attendees
                    user.save()
                    message = f'A record was updated for user: {user}, attendees: {attendees}'
                else:
                    message = f'Event {event} is at capacity'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except:
                message = f'There was an error updating booking'
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
            eventID = serializer.validated_data.get('event')
            attendees = serializer.validated_data.get('attendees')
            count = EventRegistration.objects.filter(
                eventID=eventID).aggregate(Sum('attendees'))['attendees__sum']
            if count == None:
                count = 0
            try:
                event = Event.objects.get(id=eventID)
                if EventRegistration.objects.filter(userID=user, eventID=event):
                    return Response({'message': f'user {user.name} already has a booking for event {event}'}, status=status.HTTP_403_FORBIDDEN)
                if ((count + attendees) <= event.maxAttendees):
                    new_record = EventRegistration(
                        eventID=event, userID=user, attendees=attendees)
                    new_record.save()
                    message = f'A new record was added, user: {user}, event: {eventID}, attendees: {attendees}'
                else:
                    message = f'Event {event.name} is at capacity {event.maxAttendees}'
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
