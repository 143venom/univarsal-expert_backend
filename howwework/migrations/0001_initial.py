# Generated by Django 5.1 on 2024-08-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HowWeWorkMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('background_image', models.ImageField(default='work_ethics/bg/default.jpg', upload_to='work_ethics/bg')),
            ],
        ),
        migrations.CreateModel(
            name='WorkEthic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='work_ethics/default.jpg', upload_to='work_ethics')),
            ],
        ),
    ]