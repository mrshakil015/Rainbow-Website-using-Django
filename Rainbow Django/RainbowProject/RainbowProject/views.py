from django.shortcuts import render, redirect

def homePage(request):
    
    return render(request,'commons/index.html')

def studentSignin(request):
    
    return render(request,'students/studentlogin.html')

def aboutUs(request):
    
    return render(request,'commons/aboutus.html')