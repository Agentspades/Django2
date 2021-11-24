from django.shortcuts import render
from rest_framework.decorators import api_view

from Tips.models import TipModel
from datetime import datetime
from rest_framework.response import Response
from .serializers import TipSerializer

# Create your views here.


@api_view(['POST'])
def NewTip(request):
    tip = request.data.get('tip')
    try:
        new_tip = TipModel.objects.latest()
        new_tip.tip = tip
        new_tip.save()
        return Response({'Status': '200 OK'})
    except:
        return Response({'Status': '400 Bad Request'})


@api_view(['GET'])
def GetTip(request):
    try:
        tip = TipModel.objects.latest()
        return Response({'Tip': TipSerializer(tip).data})
    except:
        return Response({'error': 'No tip has been set'})
