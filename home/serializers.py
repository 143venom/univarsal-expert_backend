from rest_framework import serializers
from .models import *


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"


class MainContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainContent
        fields = "__all__"


# class AboutSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = About
#         fields = '__all__'


# class ServiceSectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceSection
#         fields = '__all__'


# class ServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value