from django.shortcuts import render


#import datetime
from .models import Contact
from django.http import HttpResponse

def index(request):
    if request.method=='POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse('Thanks for your contact')
    return render(request,'shop/index.html')


# Create your views here.
