# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(
    r"how-we-work-title", HowWeWorkTitleViewSet, basename="how-we-work-title"
)
router.register(r"how-we-work-main", HowWeWorkMainViewSet)
router.register(r"work-ethics", WorkEthicViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
