from django.contrib import admin
from django.urls import path
from RainbowProject.views import *
from RainbowProject.studentviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage, name='homePage'),
    path('studentSignin/',studentSignin, name='studentSignin'),
    path('adminSignUP/',adminSignUP, name='adminSignUP'),
    path('adminSignin/',adminSignin, name='adminSignin'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    
    path('adminDashboard/',adminDashboard, name='adminDashboard'),
    
    #--------------Student Section-----------
    path('addStudentPage/',addStudentPage, name='addStudentPage'),
    path('studentList/',studentList, name='studentList'),
    
    
    
    path('aboutUs/',aboutUs, name='aboutUs'),
    path('contactUsPage/',contactUsPage, name='contactUsPage'),
    path('coursePage/',coursePage, name='coursePage'),
    path('servicePage/',servicePage, name='servicePage'),
    path('galleryPage/',galleryPage, name='galleryPage'),
    path('admissionformPage/',admissionformPage, name='admissionformPage'),
]
