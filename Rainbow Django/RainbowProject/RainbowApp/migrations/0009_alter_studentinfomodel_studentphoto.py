# Generated by Django 5.0.6 on 2024-06-04 18:49

import RainbowApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RainbowApp', '0008_alter_admissionformmodel_studentphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfomodel',
            name='StudentPhoto',
            field=models.ImageField(null=True, upload_to=RainbowApp.models.user_directory_path),
        ),
    ]