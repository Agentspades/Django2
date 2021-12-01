from rest_framework import serializers
from .models import ChallengeRewards, Challenges
from Auth.models import User

# class ChallengeList(serializers.ModelSerializer):
#    class Meta:
#        model = Challenges
#        fields = '__all__'


class ChallengeSerializer(serializers.Serializer):
    ChallengeID = serializers.IntegerField()
    Challenge_Title = serializers.CharField(max_length=45)
    Challenge_Description = serializers.CharField(max_length=200)
    Commencement = serializers.DateTimeField()
    Termination = serializers.DateTimeField()
    Reward = serializers.PrimaryKeyRelatedField(
        queryset=ChallengeRewards.objects.all())


class UserHasChallengesSerializer(serializers.Serializer):
    # Must change userid to current user model's query set
    UserID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    Completion = serializers.DateTimeField()
    ChallengeID = serializers.PrimaryKeyRelatedField(
        queryset=Challenges.objects.all())
