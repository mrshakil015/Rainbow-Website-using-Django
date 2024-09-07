from django.contrib import admin
from RainbowApp.models import *

# Register your models here.
class CustomUserModelDisplay(admin.ModelAdmin):
    list_display = ['username','UserType']
    search_fields = ['username','email']
    fieldsets = [
        (
            "User Information",
            {"fields":["username","email","password","UserType"]}
        )
    ]

admin.site.register(CustomUserModel,CustomUserModelDisplay)

class StudentInfoDisplay(admin.ModelAdmin):
    list_display = ['user','StudentName','CourseName']
admin.site.register(StudentInfoModel,StudentInfoDisplay)    
    
class ExamInfoDisplay(admin.ModelAdmin):
    list_display = ['Candidate','ExamTitle','TotalExamMark']
admin.site.register(ExamResultModel,ExamInfoDisplay)    
    

class PendingStudentDisplay(admin.ModelAdmin):
    list_display = ['StudentName','CourseName']
admin.site.register(AdmissionFormModel,PendingStudentDisplay)    
    
class CourseInfoDisplay(admin.ModelAdmin):
    list_display = ['CourseName','CourseDuration']
admin.site.register(CourseInfoModel,CourseInfoDisplay)

class ServiceInfoDisplay(admin.ModelAdmin):
    list_display = ['ServiceName']
admin.site.register(ServiceInfoModel,ServiceInfoDisplay)

class SuccessfulStudentDisplay(admin.ModelAdmin):
    list_display = ['id','StudentName','StudentDesignation']
admin.site.register(SuccessfulStudentInfoModel,SuccessfulStudentDisplay)

class GalleryImageDisplay(admin.ModelAdmin):
    list_display = ['id','ImageTitle']
admin.site.register(GalleryImageModel,GalleryImageDisplay)

class BatchInfoDisplay(admin.ModelAdmin):
    list_display = ['BatchNo','Batchschedule','BatchStart']
admin.site.register(BatchInfoModel,BatchInfoDisplay)

class ContactDisplay(admin.ModelAdmin):
    list_display = ['Address','Email','Mobile']
admin.site.register(ContactUsModel,ContactDisplay)
admin.site.register(BlogFileModel)
admin.site.register(BlogVideoModel)

