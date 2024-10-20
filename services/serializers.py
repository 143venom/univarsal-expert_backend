from rest_framework import serializers
from .models import *


class ServiceTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTitle
        fields = "__all__"


class ServiceContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContents
        fields = "__all__"


class ServicesSerializer(serializers.ModelSerializer):
    servicecontents = ServiceContentsSerializer(many=True, source="servicecontents_set")

    class Meta:
        model = Services
        fields = ["id", "service_name", "servicecontents"]
