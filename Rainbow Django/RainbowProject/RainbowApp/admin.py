from django.contrib import admin
from RainbowApp.models import *

# Register your models here.
class CustomUserModelDisplay(admin.ModelAdmin):
    list_display = ['username','UserType']

admin.site.register(CustomUserModel,CustomUserModelDisplay)

