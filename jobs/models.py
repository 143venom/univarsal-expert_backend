from django.db import models

from django.core.exceptions import ValidationError

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    company_profile_pic = models.ImageField(
        upload_to="jobs/company",
        default="jobs/company/default.jpg",
        blank=True,
        null=True,
    )
    company_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class JobType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class JobEducationLevel(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    PUBLISHED = "P"
    UNPUBLISHED = "U"
    STATUS_CHOICES = [
        (PUBLISHED, "Published"),
        (UNPUBLISHED, "Unpublished"),
    ]

    COVER_LETTER_CHOICES = [
        ("R", "Required"),
        ("N", "Not Required"),
    ]

    title = models.CharField(max_length=200)
    vacancy = models.IntegerField()
    location = models.ForeignKey(
        Country, related_name="locations", on_delete=models.CASCADE
    )

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company"
    )
    offer_salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.CharField(max_length=50)
    job_type = models.ForeignKey(
        JobType, on_delete=models.CASCADE, blank=True, null=True
    )
    post_date = models.DateField()
    valid_until = models.DateField()
    job_status = models.CharField(
        max_length=1,
        blank=False,
        null=False,
        choices=STATUS_CHOICES,
        default=PUBLISHED,
        verbose_name="Job Status",
        db_index=True,
    )

    qualification_required = models.ForeignKey(
        JobEducationLevel, on_delete=models.CASCADE, blank=True, null=True
    )
    preferred_age = models.CharField(max_length=50, blank=True, null=True)
    cover_letter_required = models.CharField(
        max_length=1,
        choices=COVER_LETTER_CHOICES,
        default="N",
        verbose_name="Cover Letter Requirement",
        db_index=True,
    )

    description = models.TextField()

    def clean(self):
        if self.valid_until <= self.post_date:
            raise ValidationError("Valid until date must be after the post date.")

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, related_name="applications", on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to="images/job/resumes/")
    cover_letter = models.TextField(blank=True)
    application_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"
