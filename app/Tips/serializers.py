from rest_framework import serializers
from .models import TipModel


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipModel
        fields = ['tip']
