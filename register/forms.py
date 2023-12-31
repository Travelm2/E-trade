#from django.models import models
from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.boundfield import BoundField

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    
