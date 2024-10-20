# serializers.py
from rest_framework import serializers
from .models import *


class HowWeWorkTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWeWorkTitle
        fields = "__all__"


class HowWeWorkMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWeWorkMain
        fields = "__all__"


class WorkEthicSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkEthic
        fields = "__all__"
