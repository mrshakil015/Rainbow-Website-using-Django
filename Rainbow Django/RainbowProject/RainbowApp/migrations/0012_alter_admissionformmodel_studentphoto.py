# Generated by Django 5.0.6 on 2024-06-05 16:26

import RainbowApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RainbowApp', '0011_rename_mcq_examresultmodel_obtainmcq_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionformmodel',
            name='StudentPhoto',
            field=models.ImageField(null=True, upload_to=RainbowApp.models.pending_student_dict),
        ),
    ]