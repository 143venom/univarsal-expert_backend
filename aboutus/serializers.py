from rest_framework import serializers
from .models import *


class AboutUsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsTitle
        fields = "__all__"


class AboutUsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsList
        fields = ("id", "title")


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = "__all__"


class AboutUsTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsTeam
        fields = "__all__"
