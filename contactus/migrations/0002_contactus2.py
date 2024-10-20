# Generated by Django 5.1 on 2024-08-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/contactus/icon/')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]