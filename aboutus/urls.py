from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r"about-us-title", AboutUsTitleViewSet, basename="about-us-title")
router.register(r"aboutus", AboutUsViewSet, basename="aboutus")
router.register(r"aboutus-list", AboutUsListViewSet, basename="aboutus-list")
router.register(r"aboutus-team", AboutUsTeamViewSet, basename="aboutus-team")

urlpatterns = [
    path("", include(router.urls)),
]
