# Generated by Django 5.0.6 on 2024-05-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RainbowApp', '0007_galleryimagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingStudentInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=100)),
                ('StudentName', models.CharField(max_length=100)),
                ('FatherName', models.CharField(max_length=100)),
                ('MotherName', models.CharField(max_length=100)),
                ('DOB', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('StudentPhoto', models.ImageField(upload_to='static/pendingstudent/')),
            ],
        ),
    ]