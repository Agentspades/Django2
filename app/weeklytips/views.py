from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # HTTP STATUS codes
from rest_framework import viewsets
from weeklytips import serializers
from weeklytips import models

# Create your views here.


class PostTips(APIView):
    serializer_class = serializers.TipsModelSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if models.SustainableTips.objects.all().exists():
            if serializer.is_valid():
                title = serializer.validated_data.get('title')
                description = serializer.validated_data.get('description')
                try:
                    oldTip = models.SustainableTips.objects.last()
                    oldTip.title = title
                    oldTip.description = description
                    oldTip.date_added = datetime.now().date()
                    oldTip.save()
                    message = f'A new Tip was updated, Title: {title}, Description: {description}'
                except:
                    message = f'There was an error updating Title: {title}, Description: {description}'
                return Response({'message': message})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                title = serializer.validated_data.get('title')
                description = serializer.validated_data.get('description')
                date = datetime.now().date()
                try:
                    newTip = models.SustainableTips(
                        title=title, description=description, date_added=date)
                    newTip.save()
                    message = f'A new Tip was added, Title: {title}, Description: {description}'
                except:
                    message = f'There was an error Adding Title: {title}, Description: {description}'
                return Response({'message': message})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##VIEWSET##

class TipsViewSet (viewsets.ModelViewSet):
    queryset = models.SustainableTips.objects.all()
    serializer_class = serializers.TipsModelSerializer
    http_method_names = ['get']
