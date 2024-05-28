from django.contrib import admin
from RainbowApp.models import *

# Register your models here.
class CustomUserModelDisplay(admin.ModelAdmin):
    list_display = ['username','UserType']

admin.site.register(CustomUserModel,CustomUserModelDisplay)

class CourseInfoDisplay(admin.ModelAdmin):
    list_display = ['CourseName','CourseDuration']

admin.site.register(CourseInfoModel,CourseInfoDisplay)

class ServiceInfoDisplay(admin.ModelAdmin):
    list_display = ['ServiceName']

admin.site.register(ServiceInfoModel,ServiceInfoDisplay)

class SuccessfulStudentDisplay(admin.ModelAdmin):
    list_display = ['StudentName','StudentDesignation']

admin.site.register(SuccessfulStudentInfoModel,SuccessfulStudentDisplay)

