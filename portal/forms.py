from django.forms import ModelForm

from .models import Complaint

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ComplaintForm(ModelForm):
    class Meta:
        model=Complaint
        fields =['title','area','Department','details','student']

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']