from django.db import models
from core.models import baseModel
from django.contrib.auth.models import User


# Create your models here.
class BlogTitle(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}{self.sub_title}"


class BlogPosts(baseModel):
    Active = "A"
    Inactive = "I"
    STATUS_CHOICES = [
        (Active, "Active"),
        (Inactive, "Inactive"),
    ]
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/blog/posts")
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default="Active",
        help_text="Status of the blog post",
    )
    conclusion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author.username} {self.get_status_display()}"
