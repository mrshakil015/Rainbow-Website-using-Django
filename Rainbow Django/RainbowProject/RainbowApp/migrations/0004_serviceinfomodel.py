# Generated by Django 5.0.6 on 2024-05-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RainbowApp', '0003_alter_courseinfomodel_aboutcourse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=100)),
                ('AboutService', models.TextField()),
            ],
        ),
    ]
