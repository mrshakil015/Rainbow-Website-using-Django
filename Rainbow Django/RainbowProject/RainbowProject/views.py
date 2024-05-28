from django.shortcuts import render, redirect
from RainbowApp.models import *

def homePage(request):
    courseData = CourseInfoModel.objects.all()
    serviceData = ServiceInfoModel.objects.all()
    successStudentData = SuccessfulStudentInfoModel.objects.all()
    galleryData = GalleryImageModel.objects.all()
    
    context = {
        'courseData': courseData,
        'serviceData': serviceData,
        'successStudentData': successStudentData,
        'galleryData': galleryData,
    }
    
    return render(request,'commons/index.html',context)

def adminSignin(request):
    
    return render(request,'myadmin/adminlogin.html')

def studentSignin(request):
    
    return render(request,'students/studentlogin.html')

def aboutUs(request):
    
    return render(request,'commons/aboutus.html')

def coursePage(request):
    courseData = CourseInfoModel.objects.all()
    
    context = {
        'courseData': courseData,
    }
    
    return render(request,'course/coursepage.html',context)

def servicePage(request):
    serviceData = ServiceInfoModel.objects.all()
    
    context = {
        'serviceData': serviceData,
    }
    
    return render(request,'ourservice/servicepage.html',context)

def galleryPage(request):
    galleryData = GalleryImageModel.objects.all()
    
    context = {
        'galleryData': galleryData,
    }
    
    return render(request,'gallery/gallerypage.html',context)


def contactUsPage(request):
    
    return render(request,'commons/contactus.html')

def admissionformPage(request):
    if request.method == 'POST':
        coursename = request.POST.get('coursename')
        studentname = request.POST.get('studentname')
        fathername = request.POST.get('fathername')
        mothername = request.POST.get('mothername')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        studentphoto = request.FILES.get('studentphoto')
        
        admissiondata = AdmissionFormModel(
            CourseName=coursename,
            StudentName=studentname,
            FatherName=fathername,
            MotherName=mothername,
            DOB=dob,
            Gender=gender,
            email=email,
            Mobile=mobile,
            Address=address,
            StudentPhoto=studentphoto,
        )
        admissiondata.save()
        return redirect('homePage')
        
    return render(request,'students/admissionform.html')