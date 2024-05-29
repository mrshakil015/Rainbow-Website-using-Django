from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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

def adminSignUP(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword:
            user = CustomUserModel.objects.create_user(username=username,password=password)
            user.email = email
            user.UserType = 'Admin'
            
            user.save()
            return redirect('adminSignin')
        else:
            return redirect('homePage')
    
    return render(request,'myadmin/adminregister.html')

def adminSignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("User name is: ",username)
        print("Password is: ",password)
        
        user = authenticate(username=username,password=password)
        print("User is :",user)
        if user:
            if user.UserType == 'Admin':
                login(request,user)
                return redirect('adminDashboard')
        else:
            return redirect('homePage')
    
    return render(request,'myadmin/adminlogin.html')


def logoutPage(request):
    logout(request)
    return redirect('homePage')

def adminDashboard(request):
    
    return render(request,'myadmin/admindashboard.html')

def studentSignin(request):
    if request.method == 'POST':
        studentroll = request.POST.get('studentroll')
        studentpassword = request.POST.get('studentpassword')
        
        user = authenticate(username=studentroll,password=studentpassword)
        if user:
            if user.UserType == 'Student':
                login(request,user)
                return redirect('studentDashboard')
            else:
                return redirect('studentSignin')
        else:
            return redirect('studentSignin')
        
    return render(request,'students/studentlogin.html')

def studentDashboard(request):
    
   
    
    return render(request,'students/studentdashboard.html')

def aboutUs(request):
    
    return render(request,'commons/aboutus.html')

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