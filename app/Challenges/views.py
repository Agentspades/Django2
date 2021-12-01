from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .seralizers import *
from .models import Challenges, UserHasChallenges
from django.http import JsonResponse

# Create your views here.
@api_view(('GET', ))
def getAllChallenges(request):
    serializer = ChallengeSerializer(Challenges.objects.all(), many=True)
    return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED, safe=False)

@api_view(('GET', ))
def getChallenge(request, id):
    serializer = ChallengeSerializer(Challenges.objects.filter(ChallengeID=id), many=True)
    return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED, safe=False)

@api_view(('GET', ))
def getAllUsersChallenges(request, id):
    serializer = UserHasChallengesSerializer(UserHasChallenges.objects.filter(UserID=id), many=True)
    return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED, safe=False)

## WORK-IN PROGRESS ##
#@api_view(('POST', ))
#def addUserToChallenge(request, challengeid, id):
#    challenge = Challenges.objects.filter(ChallengeID=challengeid)
#    user = id # REPLACE TO USER MODEL (User.objects.filter(id=id))
#    userHasChallengesObject = UserHasChallenges(UserID = user.id, ChallengeID=challenge.ChallengeID, Completion="")
#    userHasChallengesObject.save()
