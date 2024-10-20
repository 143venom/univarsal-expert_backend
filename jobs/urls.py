from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'countries', CountryViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'jobtypes', JobTypeViewSet) 
router.register(r'jobeducationlevels', JobEducationLevelViewSet) 
router.register(r'job', JobViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]