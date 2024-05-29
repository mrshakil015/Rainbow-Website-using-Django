from django.shortcuts import render, redirect
from RainbowApp.models import *

def addCoursePage(request):
    if request.method == 'POST':
       coursename= request.POST.get('coursename') 
       courseduration= request.POST.get('courseduration') 
       weeklyclass= request.POST.get('weeklyclass') 
       coursedurationhour= request.POST.get('coursedurationhour') 
       coursedurationminute= request.POST.get('coursedurationminute') 
       coursefee= request.POST.get('coursefee') 
       aboutcourse= request.POST.get('aboutcourse') 
       coursetopics= request.POST.get('coursetopics') 
       courseimage= request.FILES.get('courseimage') 
    
    
    return render(request,'course/addcourse.html')