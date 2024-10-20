from django.db import models


# Create your models here.
class ContactUsTitle(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}{self.sub_title}"


class ContactUs(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class ContactUs2(models.Model):
    image = models.ImageField(upload_to="images/contactus/icon/")
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"


class VisitUs(models.Model):
    embed_map_url = models.URLField(
        max_length=500, help_text="URL for Google Maps embed"
    )

    def __str__(self):
        return f"Map ({self.embed_map_url})"
