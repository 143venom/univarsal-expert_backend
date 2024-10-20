from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
class AboutUsTitleViewSet(viewsets.ModelViewSet):
    queryset = AboutUsTitle.objects.all()
    serializer_class = AboutUsTitleSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsListViewSet(viewsets.ModelViewSet):
    queryset = AboutUsList.objects.all()
    serializer_class = AboutUsListSerializer


class AboutUsTeamViewSet(viewsets.ModelViewSet):
    queryset = AboutUsTeam.objects.all()
    serializer_class = AboutUsTeamSerializer
