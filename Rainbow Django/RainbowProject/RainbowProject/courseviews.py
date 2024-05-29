from django.shortcuts import render, redirect
from RainbowApp.models import *

def addCoursePage(request):
    
    
    return render(request,'course/addcourse.html')