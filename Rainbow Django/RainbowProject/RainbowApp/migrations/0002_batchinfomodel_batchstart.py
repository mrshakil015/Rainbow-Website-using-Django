# Generated by Django 5.0.6 on 2024-05-31 17:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RainbowApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchinfomodel',
            name='BatchStart',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]