# Generated by Django 5.0.6 on 2024-05-28 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RainbowApp', '0008_pendingstudentinfomodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PendingStudentInfoModel',
            new_name='AdmissionFormModel',
        ),
    ]