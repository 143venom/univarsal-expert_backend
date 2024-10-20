from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class BlogTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTitle
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class BlogPostsSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = BlogPosts
        fields = "__all__"

    def create(self, validated_data):
        return BlogPosts.objects.create(**validated_data)
