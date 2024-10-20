from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name']


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['name']


class JobEducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobEducationLevel
        fields = ['name']


class JobSerializer(serializers.ModelSerializer):
    company_profile_pic = serializers.ImageField(source='company.company_profile_pic')
    location = CountrySerializer()
    company = CompanySerializer() 
    job_type = JobTypeSerializer() 
    qualification_required = JobEducationLevelSerializer()


    class Meta:
        model = Job
        fields = '__all__'

    def validate(self, data):
        job_instance = Job(**data)
        job_instance.clean()
        return data
        
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'