# Generated by Django 5.0.6 on 2024-05-31 17:28

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchNo', models.CharField(max_length=100)),
                ('Batchschedule', models.CharField(choices=[('09:00 AM - 10:00 AM', '09:00 AM - 10:00 AM'), ('10:00 AM - 11:30 AM', '10:00 AM - 11:30 AM'), ('11:30 AM - 01:00 PM', '11:30 AM - 01:00 PM'), ('01:00 PM - 02:30 PM', '01:00 PM - 02:30 PM'), ('03:00 PM - 04:30 PM', '03:00 PM - 04:30 PM'), ('04:30 PM - 06:00 PM', '04:30 PM - 06:00 PM'), ('06:00 PM - 07:30 PM', '06:00 PM - 07:30 PM'), ('08:00 PM - 09:30 PM', '08:00 PM - 09:30 PM')], max_length=100)),
                ('Section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=100)),
                ('CourseDuration', models.CharField(max_length=100)),
                ('WeeklyClass', models.CharField(max_length=100)),
                ('ClassDurationHour', models.CharField(max_length=100)),
                ('ClassDurationMinute', models.CharField(max_length=100)),
                ('CourseFee', models.CharField(max_length=100)),
                ('AboutCourse', models.TextField()),
                ('CourseTopics', models.TextField()),
                ('CourseImage', models.ImageField(upload_to='courseImg')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageTitle', models.CharField(max_length=100)),
                ('GalleryImage', models.ImageField(upload_to='galleryImage')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=100)),
                ('AboutService', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SuccessfulStudentInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=100)),
                ('StudentDesignation', models.CharField(max_length=100)),
                ('StudentInstitute', models.CharField(max_length=100)),
                ('StudentImage', models.ImageField(upload_to='successStudent')),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=100)),
                ('FatherName', models.CharField(max_length=100)),
                ('MotherName', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('StudentPhoto', models.ImageField(upload_to='pendingstudent')),
                ('CourseName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RainbowApp.courseinfomodel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('UserType', models.CharField(choices=[('Admin', 'Admin'), ('Student', 'Student')], max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=100)),
                ('FatherName', models.CharField(max_length=100)),
                ('MotherName', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('DOB', models.DateField()),
                ('Religion', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('EmergencyMobile', models.CharField(max_length=100)),
                ('StudentPhoto', models.ImageField(upload_to='studentphoto')),
                ('PresentAddress', models.CharField(max_length=100)),
                ('PermanentAddress', models.CharField(max_length=100)),
                ('RollNo', models.CharField(max_length=100)),
                ('CourseFee', models.CharField(max_length=100)),
                ('Payment', models.CharField(max_length=100)),
                ('Due', models.CharField(max_length=100)),
                ('AdmissionDate', models.DateField(auto_now_add=True)),
                ('LastModified', models.DateField(auto_now=True)),
                ('BatchNo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RainbowApp.batchinfomodel')),
                ('CourseName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RainbowApp.courseinfomodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
