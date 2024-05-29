from django.shortcuts import render, redirect
from RainbowApp.models import *
from django.contrib import messages

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
      
      if CourseInfoModel.objects.filter(CourseName=coursename).exists():
         messages.warning(request,'Course already exist.')
      else:
         courseData = CourseInfoModel(
            CourseName = coursename,
            CourseDuration =courseduration,
            WeeklyClass =weeklyclass,
            ClassDurationHour =coursedurationhour,
            ClassDurationMinute =coursedurationminute,
            CourseFee =coursefee,
            NoOfStudents ='০',
            AboutCourse =aboutcourse,
            CourseTopics=coursetopics,
            CourseImage=courseimage,
         )
         courseData.save()
         messages.success(request,'Course Successfully Added.')
         return redirect('courseList')
   return render(request,'course/addcourse.html')
 
def courseList(request):
   courseinfo = CourseInfoModel.objects.all()
   
   context = {
      'courseinfo':courseinfo,
   }
   
   return render(request,'course/courselist.html',context)

def editCoursePage(request,myid):
   courseinfo = CourseInfoModel.objects.get(id=myid)
   
   context = {
      'courseinfo':courseinfo,
   }
   
   
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

      if courseimage:
         CourseInfoModel.objects.filter(id=myid).update(
            CourseName = coursename,
            CourseDuration =courseduration,
            WeeklyClass =weeklyclass,
            ClassDurationHour =coursedurationhour,
            ClassDurationMinute =coursedurationminute,
            CourseFee =coursefee,
            AboutCourse =aboutcourse,
            CourseTopics=coursetopics,
            CourseImage=courseimage,
         )
      else:
         courseData = CourseInfoModel.objects.get(id=myid)
         previImg = courseData.CourseImage
         print("Previous Img")
         CourseInfoModel.objects.filter(id=myid).update(
            CourseName = coursename,
            CourseDuration =courseduration,
            WeeklyClass =weeklyclass,
            ClassDurationHour =coursedurationhour,
            ClassDurationMinute =coursedurationminute,
            CourseFee =coursefee,
            AboutCourse =aboutcourse,
            CourseTopics=coursetopics,
            CourseImage=previImg,
         )
      return redirect('courseList')
         
   return render(request,'course/editcourse.html',context)

def deleteCourse(request,myid):
   courseData = CourseInfoModel.objects.get(id=myid)
   courseData.delete()
   return redirect('courseList')

def coursePage(request):
    courseData = CourseInfoModel.objects.all()
    
    context = {
        'courseData': courseData,
    }
    
    return render(request,'course/coursepage.html',context)

def viewCourse(request,courseid):
   courseData = CourseInfoModel.objects.get(id=courseid)
   context = {
      'courseData':courseData
   }
   
   return render(request,'course/viewcourse.html',context)