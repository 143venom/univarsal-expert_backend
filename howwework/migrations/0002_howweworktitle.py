# Generated by Django 5.1 on 2024-08-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howwework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowWeWorkTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
            ],
        ),
    ]