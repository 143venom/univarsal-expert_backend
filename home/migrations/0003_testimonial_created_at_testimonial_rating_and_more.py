# Generated by Django 5.1 on 2024-08-20 08:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, default='home/testimonial/default.jpg', null=True, upload_to='home/testimonial'),
        ),
    ]