# Generated by Django 5.0.6 on 2024-05-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RainbowApp', '0009_rename_pendingstudentinfomodel_admissionformmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionformmodel',
            name='DOB',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='admissionformmodel',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]