from django.db import models


# Create your models here.
class HowWeWorkTitle(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}{self.sub_title}"


class HowWeWorkMain(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    background_image = models.ImageField(
        upload_to="work_ethics/bg", default="work_ethics/bg/default.jpg"
    )

    def __str__(self):
        return self.title


class WorkEthic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to="work_ethics", default="work_ethics/default.jpg"
    )

    def __str__(self):
        return self.title
