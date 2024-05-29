from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USERTYPE = [
        ('Admin','Admin'),
        ('Student','Student'),
    ]
    UserType = models.CharField(choices=USERTYPE,max_length=100)

class StudentInfoModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete =models.CASCADE,related_name='studentuser')
    StudentName = models.CharField(max_length=100)
    FatherName = models.CharField(max_length=100)
    MotherName = models.CharField(max_length=100)
    GENDER = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    
    Gender = models.CharField(choices=GENDER,max_length=100)
    DOB = models.DateField()
    Religion = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)
    EmergencyMobile = models.CharField(max_length=100)
    StudentPhoto = models.ImageField(upload_to='static/pendingstudent/')
    PresentAddress = models.CharField(max_length=100)
    PermanentAddress = models.CharField(max_length=100)
    RollNo = models.CharField(max_length=100)
    CourseName = models.CharField(max_length=100) 
    Batch = models.CharField(max_length=100)
    
    SECTION = [
        ('A','A'),
        ('B','B'),
        ('C','C'),
    ]
    
    Section = models.CharField(max_length=100)
    CourseFee = models.CharField(max_length=100)
    Payment = models.CharField(max_length=100)
    Due = models.CharField(max_length=100)
    AdmissionDate = models.DateField(auto_now_add=True)
    LastModified = models.DateField(auto_now=True)
    
    
    
class AdmissionFormModel(models.Model):
    CourseName = models.CharField(max_length=100)
    StudentName = models.CharField(max_length=100)
    FatherName = models.CharField(max_length=100)
    MotherName = models.CharField(max_length=100)
    DOB = models.DateField()
    
    GENDER = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    
    Gender = models.CharField(choices=GENDER,max_length=100)
    email = models.EmailField(max_length=100)
    Mobile = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    StudentPhoto = models.ImageField(upload_to='static/pendingstudent/')
    
class CourseInfoModel(models.Model):
    CourseName = models.CharField(max_length=100)
    CourseDuration = models.CharField(max_length=100)
    WeeklyClass = models.CharField(max_length=100)
    ClassDurationHour = models.CharField(max_length=100)
    ClassDurationMinute = models.CharField(max_length=100)
    CourseFee = models.CharField(max_length=100)
    NoOfStudents = models.CharField(max_length=100)
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
    StudentImage = models.ImageField(upload_to='static/successStudent/')
    
class GalleryImageModel(models.Model):
    ImageTitle = models.CharField(max_length=100)
    GalleryImage = models.ImageField(upload_to='static/galleryImage/')