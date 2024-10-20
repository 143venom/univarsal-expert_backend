from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


class MainContentViewSet(viewsets.ModelViewSet):
    queryset = MainContent.objects.all()
    serializer_class = MainContentSerializer


# class AboutViewSet(viewsets.ModelViewSet):
#     queryset = About.objects.all()
#     serializer_class = AboutSerializer


# class ServiceSectionViewSet(viewsets.ModelViewSet):
#     queryset = ServiceSection.objects.all()
#     serializer_class = ServiceSectionSerializer


# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
