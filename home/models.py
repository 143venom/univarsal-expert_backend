from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.
class Logo(models.Model):
    logo = models.ImageField(upload_to="logo", null=True, blank=True)

    def __str__(self):
        return "Site Logo"


class MainContent(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    bg_image = models.ImageField(upload_to="home/main", default="home/main/default.jpg")

    def __str__(self):
        return self.title


# class About(models.Model):
#     title = models.CharField(max_length=255)
#     subtitle = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(upload_to='home/about_us', default="home/about_us/default.jpg")

#     def __str__(self):
#         return self.title


# class ServiceSection(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()

#     def __str__(self):
#         return self.title


# class Service(models.Model):
#     services = models.ForeignKey(ServiceSection, related_name='services', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(upload_to='home/services', default="home/services/default.jpg")

#     def __str__(self):
#         return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=1)
    description = models.TextField()
    image = models.ImageField(upload_to='home/testimonial', default="home/testimonial/default.jpg", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
