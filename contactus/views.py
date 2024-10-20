import logging
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

logger = logging.getLogger(__name__)


# Create your views here.
class ContactUsTitleViewSet(viewsets.ModelViewSet):
    queryset = ContactUsTitle.objects.all()
    serializer_class = ContactUsTitleSerializer


class ContactUsContentViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsContentSerializer


class ContactUs2ViewSet(viewsets.ModelViewSet):
    queryset = ContactUs2.objects.all()
    serializer_class = ContactUs2Serializer


class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_create(self, serializer):
        submission = serializer.save()
        try:
            # Send notification to admin
            admin_subject = "New Contact Form Submission"
            admin_message = render_to_string(
                "contact_form_submission.html",
                {
                    "subject": submission.subject,
                    "message": submission.message,
                    "email": submission.email,
                },
            )
            admin_email = EmailMessage(
                subject=admin_subject,
                body=admin_message,
                from_email=submission.email,
                to=["info@universalexperthr.com"],
            )
            admin_email.content_subtype = "html"
            admin_email.send(fail_silently=False)

            # Send reply notification to sender
            reply_subject = "Thank you for your message!"
            reply_message = render_to_string(
                "reply_notification.html",
                {
                    "subject": submission.subject,
                    "message": submission.message,
                },
            )
            reply_email = EmailMessage(
                subject=reply_subject,
                body=reply_message,
                from_email="info@universalexperthr.com",
                to=[submission.email],
            )
            reply_email.content_subtype = "html"
            reply_email.send(fail_silently=False)

        except Exception as e:
            logger.error(
                f"Failed to send mail for submission {submission.id}: {e}",
                exc_info=True,
            )
            raise Exception(
                "There was an issue sending your message. Please try again later."
            )


class VisitUsViewSet(viewsets.ModelViewSet):
    queryset = VisitUs.objects.all()
    serializer_class = VisitUsSerializer
