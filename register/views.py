
from django.shortcuts import  render, redirect
#from django.http import HttpResponse
#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import login, authenticate
#from .forms import RegisterForm
#https://www.techwithtim.net/tutorials/django/user-registration
from .forms import RegisterForm

# Create your views here.
def register(request):
        if request.method == "POST":
                form = RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                return redirect("/")
        else:
                form =RegisterForm ()
        return render (request, "shop/register.html", {"form":form})
