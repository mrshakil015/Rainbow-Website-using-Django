from django.shortcuts import render, redirect
from RainbowApp.models import *

def homePage(request):
    courseData = CourseInfoModel.objects.all()
    serviceData = ServiceInfoModel.objects.all()
    successStudentData = SuccessfulStudentInfoModel.objects.all()
    
    context = {
        'courseData': courseData,
        'serviceData': serviceData,
        'successStudentData': successStudentData,
    }
    
    return render(request,'commons/index.html',context)

def studentSignin(request):
    
    return render(request,'students/studentlogin.html')

def aboutUs(request):
    
    return render(request,'commons/aboutus.html')

# def coursePage()