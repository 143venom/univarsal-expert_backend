# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'logos', LogoViewSet)
router.register(r'main-content', MainContentViewSet)
# router.register(r'abouts', AboutViewSet)
# router.register(r'service-sections', ServiceSectionViewSet)
# router.register(r'services', ServiceViewSet)
router.register(r'testimonials', TestimonialViewSet)


urlpatterns = [
    path('', include(router.urls)),
]