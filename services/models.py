from django.db import models


# Create your models here.
class ServiceTitle(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}{self.sub_title}"


class Services(models.Model):
    service_name = models.CharField(max_length=100)

    def __str__(self):
        return self.service_name


class ServiceContents(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    title_1 = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/servicecontents/")
    description_1 = models.TextField()
    title_2 = models.CharField(max_length=100)
    description_2 = models.TextField()

    def __str__(self):
        return self.title_1
