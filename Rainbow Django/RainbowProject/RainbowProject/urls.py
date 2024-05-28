from django.contrib import admin
from django.urls import path
from RainbowProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage, name='homePage'),
    path('studentSignin/',studentSignin, name='studentSignin'),
    
    
    path('aboutUs/',aboutUs, name='aboutUs'),
    path('coursePage/',coursePage, name='coursePage'),
]
