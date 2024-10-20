from django.db import models


# Create your models here.
class AboutUsTitle(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}{self.sub_title}"


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/aboutus/aboutus")

    def __str__(self):
        return self.title


class AboutUsList(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class AboutUsTeam(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/aboutus/team/")

    def __str__(self):
        return self.name
