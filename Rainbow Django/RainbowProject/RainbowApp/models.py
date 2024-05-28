from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USERTYPE = [
        ('Admin','Admin'),
        ('Student','Student'),
    ]
    UserType = models.CharField(choices=USERTYPE,max_length=100)
    
class CourseInfoModel(models.Model):
    CourseName = models.CharField(max_length=100)
    CourseDuration = models.CharField(max_length=100)
    WeeklyClass = models.CharField(max_length=100)
    ClassDurationHour = models.CharField(max_length=100)
    ClassDurationMinute = models.CharField(max_length=100)
    CourseFee = models.CharField(max_length=100)
    AboutCourse = models.TextField()
    CourseTopics = models.TextField()
    CourseImage = models.ImageField(upload_to='static/courseImg/')
    
class ServiceInfoModel(models.Model):
    ServiceName = models.CharField(max_length=100)
    AboutService = models.TextField()

class SuccessfulStudentInfoModel(models.Model):
    StudentName = models.CharField(max_length=100)
    StudentDesignation = models.CharField(max_length=100)
    StudentInstitute = models.CharField(max_length=100)
    CourseImage = models.ImageField(upload_to='static/successStudent/')