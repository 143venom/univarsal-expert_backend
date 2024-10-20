from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(
    r"background-image", BackgroundImageViewSet, basename="background-image"
)


urlpatterns = [
    path("", include(router.urls)),
]
