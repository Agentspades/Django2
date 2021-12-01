from django.db.models import fields
from rest_framework import serializers
from weeklytips import models


class TipsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    description = serializers.CharField(max_length=700)


class TipsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SustainableTips
        fields = '__all__'
