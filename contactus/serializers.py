from .serializers import *
from rest_framework import serializers
from .models import *


class ContactUsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsTitle
        fields = "__all__"


class ContactUsContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class ContactUs2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs2
        fields = "__all__"


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"


class VisitUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitUs
        fields = "__all__"
