from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
class ServiceTitleViewSet(viewsets.ModelViewSet):
    queryset = ServiceTitle.objects.all()
    serializer_class = ServiceTitleSerializer


class ServicesViesSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServiceContentsViewSet(viewsets.ModelViewSet):
    queryset = ServiceContents.objects.all()
    serializer_class = ServiceContentsSerializer
