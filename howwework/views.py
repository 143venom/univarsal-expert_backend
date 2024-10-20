from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
class HowWeWorkTitleViewSet(viewsets.ModelViewSet):
    queryset = HowWeWorkTitle.objects.all()
    serializer_class = HowWeWorkTitleSerializer


class HowWeWorkMainViewSet(viewsets.ModelViewSet):
    queryset = HowWeWorkMain.objects.all()
    serializer_class = HowWeWorkMainSerializer


class WorkEthicViewSet(viewsets.ModelViewSet):
    queryset = WorkEthic.objects.all()
    serializer_class = WorkEthicSerializer
