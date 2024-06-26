# Generated by Django 5.0.6 on 2024-06-05 19:30

import RainbowApp.models
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
                ('BatchNo', models.CharField(max_length=100, null=True)),
                ('Batchschedule', models.CharField(choices=[('09:00 AM - 10:00 AM', '09:00 AM - 10:00 AM'), ('10:00 AM - 11:30 AM', '10:00 AM - 11:30 AM'), ('11:30 AM - 01:00 PM', '11:30 AM - 01:00 PM'), ('01:00 PM - 02:30 PM', '01:00 PM - 02:30 PM'), ('03:00 PM - 04:30 PM', '03:00 PM - 04:30 PM'), ('04:30 PM - 06:00 PM', '04:30 PM - 06:00 PM'), ('06:00 PM - 07:30 PM', '06:00 PM - 07:30 PM'), ('08:00 PM - 09:30 PM', '08:00 PM - 09:30 PM')], max_length=100, null=True)),
                ('Section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=100, null=True)),
                ('Status', models.CharField(choices=[('Running', 'Running'), ('Completed', 'Completed')], max_length=100, null=True)),
                ('BatchStart', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=100, null=True)),
                ('Mobile', models.CharField(max_length=100, null=True)),
                ('Facebook', models.CharField(max_length=100, null=True)),
                ('MapLink', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=100, null=True)),
                ('CourseDuration', models.CharField(max_length=100, null=True)),
                ('WeeklyClass', models.CharField(max_length=100, null=True)),
                ('ClassDurationHour', models.CharField(max_length=100, null=True)),
                ('ClassDurationMinute', models.CharField(max_length=100, null=True)),
                ('CourseFee', models.CharField(max_length=100, null=True)),
                ('AboutCourse', models.TextField(null=True)),
                ('CourseTopics', models.TextField(null=True)),
                ('CourseImage', models.ImageField(null=True, upload_to='courseImg')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageTitle', models.CharField(max_length=100, null=True)),
                ('GalleryImage', models.ImageField(null=True, upload_to='galleryImage')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=100, null=True)),
                ('AboutService', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuccessfulStudentInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=100, null=True)),
                ('StudentDesignation', models.CharField(max_length=100, null=True)),
                ('StudentInstitute', models.CharField(max_length=100, null=True)),
                ('StudentImage', models.ImageField(null=True, upload_to='successStudent')),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=100, null=True)),
                ('FatherName', models.CharField(max_length=100, null=True)),
                ('MotherName', models.CharField(max_length=100, null=True)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('Mobile', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('StudentPhoto', models.ImageField(null=True, upload_to=RainbowApp.models.pending_student_dict)),
                ('CourseName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RainbowApp.courseinfomodel')),
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
                ('UserType', models.CharField(choices=[('Admin', 'Admin'), ('Student', 'Student')], max_length=100, null=True)),
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
                ('StudentName', models.CharField(max_length=100, null=True)),
                ('FatherName', models.CharField(max_length=100, null=True)),
                ('MotherName', models.CharField(max_length=100, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('DOB', models.DateField(null=True)),
                ('Religion', models.CharField(max_length=100, null=True)),
                ('Mobile', models.CharField(max_length=100, null=True)),
                ('EmergencyMobile', models.CharField(max_length=100, null=True)),
                ('StudentPhoto', models.ImageField(null=True, upload_to=RainbowApp.models.user_directory_path)),
                ('PresentAddress', models.CharField(max_length=100, null=True)),
                ('PermanentAddress', models.CharField(max_length=100, null=True)),
                ('RollNo', models.CharField(max_length=100, null=True)),
                ('Batchschedule', models.CharField(max_length=100, null=True)),
                ('Section', models.CharField(max_length=100, null=True)),
                ('CourseFee', models.CharField(max_length=100, null=True)),
                ('Payment', models.CharField(max_length=100, null=True)),
                ('Due', models.CharField(max_length=100, null=True)),
                ('AdmissionDate', models.DateField(auto_now_add=True)),
                ('LastModified', models.DateField(auto_now=True)),
                ('BatchNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='batchinfomodel', to='RainbowApp.batchinfomodel')),
                ('CourseName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courseinfomodel', to='RainbowApp.courseinfomodel')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExamResultModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExamTitle', models.CharField(max_length=100, null=True)),
                ('ObtainMCQ', models.CharField(max_length=100, null=True)),
                ('ObtainWritten', models.CharField(max_length=100, null=True)),
                ('ObtainPracticle', models.CharField(max_length=100, null=True)),
                ('ObtainTotalMark', models.CharField(max_length=100, null=True)),
                ('TotalMCQ', models.CharField(max_length=100, null=True)),
                ('TotalWritten', models.CharField(max_length=100, null=True)),
                ('TotalPracticle', models.CharField(max_length=100, null=True)),
                ('TotalExamMark', models.CharField(max_length=100, null=True)),
                ('ExamDate', models.DateField(null=True)),
                ('Candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examinfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
