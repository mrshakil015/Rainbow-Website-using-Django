from django.contrib import admin
from django.urls import path
from RainbowProject.views import *
from RainbowProject.studentviews import *
from RainbowProject.courseviews import *
from RainbowProject.batchviews import *

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
    
    path('addSuccessfulStudent/',addSuccessfulStudent, name='addSuccessfulStudent'),
    path('successStudentList/',successStudentList, name='successStudentList'),
    path('editSuccessStudent/<str:myid>',editSuccessStudent, name='editSuccessStudent'),
    path('deleteSuccessStudent/<str:myid>',deleteSuccessStudent, name='deleteSuccessStudent'),
    
    #------------Course Section----------------
    path('addCoursePage/',addCoursePage, name='addCoursePage'),
    path('courseList/',courseList, name='courseList'),
    path('editCoursePage/<str:myid>',editCoursePage, name='editCoursePage'),
    path('deleteCourse/<str:myid>',deleteCourse, name='deleteCourse'),
    path('viewCourse/<str:courseid>',viewCourse, name='viewCourse'),
    
    
    
    #-------------Common Front End-----------
    path('aboutUs/',aboutUs, name='aboutUs'),
    path('coursePage/',coursePage, name='coursePage'),
    path('servicePage/',servicePage, name='servicePage'),
    path('admissionformPage/',admissionformPage, name='admissionformPage'),
    
    #----------Gallery-------------------
    path('galleryPage/',galleryPage, name='galleryPage'),
    path('addGallery/',addGallery, name='addGallery'),
    path('galleryList/',galleryList, name='galleryList'),
    path('editImage/<str:myid>',editImage, name='editImage'),
    path('deleteImage/<str:myid>',deleteImage, name='deleteImage'),
    
    #-----------Batch---------------
    path('batchList/',batchList, name='batchList'),
    path('addBatch/',addBatch, name='addBatch'),
    path('deleteBatch/<str:myid>',deleteBatch, name='deleteBatch'),
    path('editBatch/<str:myid>',editBatch, name='editBatch'),
    path('viewSingleBatch/<str:batchno>',viewSingleBatch, name='viewSingleBatch'),
    path('batchPrint/<str:batchno>',batchPrint, name='batchPrint'),
    
    #----------Payment-----------
    path('paymentList/',paymentList, name='paymentList'),
    
    #------------Service------------
    path('serviceList/',serviceList, name='serviceList'),
    path('addService/',addService, name='addService'),
    path('editService/<str:myid>',editService, name='editService'),
    path('deleteService/<str:myid>',deleteService, name='deleteService'),
    
    #-----------Contact-------------------
    path('contactUsPage/',contactUsPage, name='contactUsPage'),
    path('contactList/',contactList, name='contactList'),
    path('addContact/',addContact, name='addContact'),
    path('editContact/<str:myid>',editContact, name='editContact'),
    path('deleteContact/<str:myid>',deleteContact, name='deleteContact'),
    
    path('admissionPage/',admissionPage, name='admissionPage'),
]

urlpatterns+=re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
urlpatterns+=re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),