from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r"blog-title", BlogTitleViewSet, basename="blog-title")
router.register(r"blog-post", BlogPostsViewSet, basename="blog-post")


urlpatterns = [
    path("", include(router.urls)),
]
