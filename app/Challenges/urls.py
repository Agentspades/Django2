from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('all_challenges/', getAllChallenges),
    url('challenge/(?P<id>\d+)/', getChallenge,),
    url('user/(?P<id>\d+)/challenges/', getAllUsersChallenges,),
    # url('challenge/(?P<challengeid>\d+)/user/(?P<id>\d+)/', addUserToChallenge)
]
