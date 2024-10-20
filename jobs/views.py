import logging
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import BadHeaderError
from .models import *
from .serializers import *

# Create your views here.

logger = logging.getLogger(__name__)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class JobTypeViewSet(viewsets.ModelViewSet):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer


class JobEducationLevelViewSet(viewsets.ModelViewSet):
    queryset = JobEducationLevel.objects.all()
    serializer_class = JobEducationLevelSerializer


class JobPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'show'  
    max_page_size = 20  


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    pagination_class = JobPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['location', 'job_type']
    ordering_fields = ['post_date', 'valid_until']
    ordering = ['post_date']
    search_fields = ['title'] 
    

    def list(self, request, *args, **kwargs):
        try:
            # Validate filter parameters
            valid_filters = set(self.filterset_fields + self.ordering_fields + self.search_fields)
            invalid_filters = set(request.query_params.keys()) - valid_filters
            
            if invalid_filters:
                return Response(
                    {'detail': f'Invalid filter parameters: {", ".join(invalid_filters)}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            queryset = self.filter_queryset(self.get_queryset())
        
            if not queryset.exists():
                return Response({'detail': 'No jobs found.'}, status=status.HTTP_404_NOT_FOUND)

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ValidationError as ve:
            logger.error(f'Validation error occurred: {str(ve)}')
            return Response({'detail': str(ve)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f'Error occurred while retrieving jobs: {str(e)}')
            return Response({'detail': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            # Send email notification
            job_title = serializer.validated_data['job'].title
            applicant_name = serializer.validated_data['applicant_name']
            email = serializer.validated_data['email']
            
            subject = f"New Job Application for {job_title}"
            message = f"""
            Dear Team,

            A new application has been submitted for the job position: {job_title}.

            Applicant Details:
            Name: {applicant_name}
            Email: {email}

            The resume and cover letter are attached.

            Best regards,
            Job Application System
            """
            recipient_list = [settings.EMAIL_HOST_USER]
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
            except BadHeaderError:
                logger.error("Invalid header found.")
            except Exception as e:
                logger.error(f"An error occurred while sending email: {e}")
            
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)