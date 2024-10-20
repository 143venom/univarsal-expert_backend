"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Universal API",
        default_version="v1",
        description="Universal Company",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=settings.DEVELOPER_EMAIL),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("aboutus.urls")),
    # path('api/v1/', include('accounts.urls')),
    path("api/v1/", include("blog.urls")),
    path("api/v1/", include("contactus.urls")),
    path("api/v1/", include("core.urls")),
    path("api/v1/", include("home.urls")),
    path("api/v1/", include("howwework.urls")),
    path("api/v1/", include("jobs.urls")),
    path("api/v1/", include("services.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Add this to include the i18n URL patterns
# urlpatterns += [
#     path('i18n/', include('django.conf.urls.i18n')),
# ]
