from django.db import models


# Create your models here.
class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def created_date(self):
        return self.created_at.date()

    @property
    def updated_date(self):
        return self.updated_at.date()


class BackgroundImage(baseModel):
    image = models.ImageField(
        upload_to="images/core/background_images/", null=True, blank=True
    )
