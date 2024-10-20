from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r"contact-us-title", ContactUsTitleViewSet, basename="contact-us-title")
router.register(r"contactus", ContactUsContentViewSet, basename="contactus-content")
router.register(r"contactus2-list", ContactUsContentViewSet, basename="contactus2-list")
router.register(r"contact-form", ContactFormViewSet, basename="contactus-form")
router.register(r"visit-us", VisitUsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
