from django.db import models
from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=150)

    #fame = models.CharField(max_length=200)
    #lname = models.CharField(max_length=50)
    email = models.CharField(max_length=90)
    subject = models.TextField()
    #date = models.CharField(max_length=12, default="")
    #time = models.CharField(max_length=12, default="")
    #message = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
