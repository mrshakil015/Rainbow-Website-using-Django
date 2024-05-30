from django.contrib import admin
from django.urls import path
from RainbowProject.views import *
from RainbowProject.studentviews import *
from RainbowProject.courseviews import *

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage, name='homePage'),
    path('studentSignin/',studentSignin, name='studentSignin'),
    path('adminSignUP/',adminSignUP, name='adminSignUP'),
    path('adminSignin/',adminSignin, name='adminSignin'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    
    path('adminDashboard/',adminDashboard, name='adminDashboard'),
    path('studentDashboard/',studentDashboard, name='studentDashboard'),
    
    #--------------Student Section-------------------------------
    path('addStudentPage/',addStudentPage, name='addStudentPage'),
    path('editStudent/<str:myid>',editStudent, name='editStudent'),
    path('deleteStudent/<str:user>',deleteStudent, name='deleteStudent'),
    path('studentList/',studentList, name='studentList'),
    path('pendingStudentList/',pendingStudentList, name='pendingStudentList'),
    path('editPendingStudent/<str:myid>',editPendingStudent, name='editPendingStudent'),
    path('admitedcourseInfo/',admitedcourseInfo, name='admitedcourseInfo'),
    path('admitedcoursePaymentInfo/',admitedcoursePaymentInfo, name='admitedcoursePaymentInfo'),
    
    #------------Course Section----------------
    path('addCoursePage/',addCoursePage, name='addCoursePage'),
    path('courseList/',courseList, name='courseList'),
    path('editCoursePage/<str:myid>',editCoursePage, name='editCoursePage'),
    path('deleteCourse/<str:myid>',deleteCourse, name='deleteCourse'),
    path('viewCourse/<str:courseid>',viewCourse, name='viewCourse'),
    
    
    
    
    path('aboutUs/',aboutUs, name='aboutUs'),
    path('contactUsPage/',contactUsPage, name='contactUsPage'),
    path('coursePage/',coursePage, name='coursePage'),
    path('servicePage/',servicePage, name='servicePage'),
    path('galleryPage/',galleryPage, name='galleryPage'),
    path('admissionformPage/',admissionformPage, name='admissionformPage'),
    
    path('paymentList/',paymentList, name='paymentList'),
]

urlpatterns+=re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
urlpatterns+=re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),