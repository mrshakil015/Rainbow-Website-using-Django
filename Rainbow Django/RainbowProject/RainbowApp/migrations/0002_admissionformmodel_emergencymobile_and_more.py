# Generated by Django 5.0.6 on 2024-06-07 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RainbowApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionformmodel',
            name='EmergencyMobile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admissionformmodel',
            name='PermanentAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admissionformmodel',
            name='Qualification',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admissionformmodel',
            name='Religion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentinfomodel',
            name='Qualification',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
