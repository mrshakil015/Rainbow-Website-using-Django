from django.contrib import admin
from django.urls import path
from RainbowProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage, name='homePage'),
    path('studentSignin/',studentSignin, name='studentSignin'),
    
    
    path('aboutUs/',aboutUs, name='aboutUs'),
    path('contactUsPage/',contactUsPage, name='contactUsPage'),
    path('coursePage/',coursePage, name='coursePage'),
    path('servicePage/',servicePage, name='servicePage'),
    path('galleryPage/',galleryPage, name='galleryPage'),
    path('admissionformPage/',admissionformPage, name='admissionformPage'),
]
