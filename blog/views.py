from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
class BlogTitleViewSet(viewsets.ModelViewSet):
    queryset = BlogTitle.objects.all()
    serializer_class = BlogTitleSerializer


class BlogPostsViewSet(viewsets.ModelViewSet):
    queryset = BlogPosts.objects.filter(status=BlogPosts.Active).order_by("-id")
    serializer_class = BlogPostsSerializer
