from django import forms
from RainbowApp.models import *
from django.contrib.auth.forms import AuthenticationForm

class BlogFileForm(forms.ModelForm):
    class Meta:
        model = BlogFileModel
        fields = "__all__"
