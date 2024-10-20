from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.


class BackgroundImageViewSet(viewsets.ModelViewSet):
    queryset = BackgroundImage.objects.all().order_by("-id")
    serializer_class = BackgroundImageSerializer
