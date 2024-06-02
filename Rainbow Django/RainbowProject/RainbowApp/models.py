from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USERTYPE = [
        ('Admin','Admin'),
        ('Student','Student'),
    ]
    UserType = models.CharField(choices=USERTYPE,max_length=100, null=True)

class CourseInfoModel(models.Model):
    CourseName = models.CharField(max_length=100, null=True)
    CourseDuration = models.CharField(max_length=100, null=True)
    WeeklyClass = models.CharField(max_length=100, null=True)
    ClassDurationHour = models.CharField(max_length=100, null=True)
    ClassDurationMinute = models.CharField(max_length=100, null=True)
    CourseFee = models.CharField(max_length=100, null=True)
    AboutCourse = models.TextField(null=True)
    CourseTopics = models.TextField(null=True)
    CourseImage = models.ImageField(upload_to='courseImg',null=True)
    
    def __str__(self):
        return self.CourseName

class BatchInfoModel(models.Model):
    BatchNo = models.CharField(max_length=100, null=True)
    SCHEDULE = [
        ('09:00 AM - 10:00 AM','09:00 AM - 10:00 AM'),
        ('10:00 AM - 11:30 AM','10:00 AM - 11:30 AM'),
        ('11:30 AM - 01:00 PM','11:30 AM - 01:00 PM'),
        ('01:00 PM - 02:30 PM','01:00 PM - 02:30 PM'),
        ('03:00 PM - 04:30 PM','03:00 PM - 04:30 PM'),
        ('04:30 PM - 06:00 PM','04:30 PM - 06:00 PM'),
        ('06:00 PM - 07:30 PM','06:00 PM - 07:30 PM'),
        ('08:00 PM - 09:30 PM','08:00 PM - 09:30 PM'),
    ]
    Batchschedule = models.CharField(choices=SCHEDULE,max_length=100, null=True)
    SECTION = [
        ('A','A'),
        ('B','B'),
        ('C','C'),
    ]
    Section = models.CharField(choices=SECTION,max_length=100, null=True)
    STATUS = [
        ('Running','Running'),
        ('Completed','Completed'),
    ]
    Status = models.CharField(choices=STATUS,max_length=100, null=True)
    BatchStart = models.DateField()
    
    def __str__(self):
        return self.BatchNo

class StudentInfoModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete =models.CASCADE,related_name='studentuser', null=True)
    StudentName = models.CharField(max_length=100, null=True)
    FatherName = models.CharField(max_length=100, null=True)
    MotherName = models.CharField(max_length=100, null=True)
    GENDER = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    
    Gender = models.CharField(choices=GENDER,max_length=100, null=True)
    DOB = models.DateField(null=True)
    Religion = models.CharField(max_length=100, null=True)
    Mobile = models.CharField(max_length=100, null=True)
    EmergencyMobile = models.CharField(max_length=100, null=True)
    StudentPhoto = models.ImageField(upload_to='studentphoto', null=True)
    PresentAddress = models.CharField(max_length=100, null=True)
    PermanentAddress = models.CharField(max_length=100, null=True)
    RollNo = models.CharField(max_length=100, null=True)
    CourseName = models.ForeignKey(CourseInfoModel,on_delete=models.SET_NULL,related_name='courseinfomodel', null=True) 
    BatchNo = models.ForeignKey(BatchInfoModel,on_delete=models.SET_NULL,related_name='batchinfomodel', null=True)
    Batchschedule = models.CharField(max_length=100, null=True)
    
    SECTION = [
        ('A','A'),
        ('B','B'),
        ('C','C'),
    ]
    
    Section = models.CharField(max_length=100, null=True) 
    CourseFee = models.CharField(max_length=100, null=True)
    Payment = models.CharField(max_length=100, null=True)
    Due = models.CharField(max_length=100, null=True)
    AdmissionDate = models.DateField(auto_now_add=True)
    LastModified = models.DateField(auto_now=True)
    
    
    
class AdmissionFormModel(models.Model):
    CourseName = models.ForeignKey(CourseInfoModel,on_delete=models.SET_NULL,null=True) 
    StudentName = models.CharField(max_length=100, null=True)
    FatherName = models.CharField(max_length=100, null=True)
    MotherName = models.CharField(max_length=100, null=True)
    DOB = models.DateField()
    
    GENDER = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    
    Gender = models.CharField(choices=GENDER,max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    Mobile = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=100, null=True)
    StudentPhoto = models.ImageField(upload_to='pendingstudent', null=True)
    

    
class ServiceInfoModel(models.Model):
    ServiceName = models.CharField(max_length=100, null=True)
    AboutService = models.TextField(null=True)

class SuccessfulStudentInfoModel(models.Model):
    StudentName = models.CharField(max_length=100, null=True)
    StudentDesignation = models.CharField(max_length=100, null=True)
    StudentInstitute = models.CharField(max_length=100, null=True)
    StudentImage = models.ImageField(upload_to='successStudent', null=True)
    
class GalleryImageModel(models.Model):
    ImageTitle = models.CharField(max_length=100, null=True)
    GalleryImage = models.ImageField(upload_to='galleryImage', null=True)
    
class ContactUsModel(models.Model):
    Address = models.CharField(max_length=200)
    Email = models.EmailField(max_length=100, null=True)
    Mobile = models.CharField(max_length=100, null=True)
    Facebook = models.CharField(max_length=100, null=True)
    MapLink = models.TextField(null=True)
    
