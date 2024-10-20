from rest_framework import serializers
from .models import *


class BackgroundImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundImage
        fields = "__all__"
