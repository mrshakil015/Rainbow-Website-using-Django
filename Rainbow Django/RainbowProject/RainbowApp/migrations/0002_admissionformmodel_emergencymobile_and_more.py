# Generated by Django 5.0.6 on 2024-06-07 14:56

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
            name='Religion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]