from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r"service-title", ServiceTitleViewSet, basename="service-title")
router.register(r"services", ServicesViesSet, basename="services")
router.register(
    r"service-contents", ServiceContentsViewSet, basename="service-contents"
)

urlpatterns = [
    path("", include(router.urls)),
]
