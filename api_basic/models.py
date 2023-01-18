from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db.models.fields import DateField
from django.db.models.query_utils import select_related_descend
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.URLField(max_length=200,null=True,blank=True)
    insta = models.CharField(max_length=100,null=True,blank=True)
    linkedIn = models.CharField(max_length=100,null=True,blank=True)
    gmail = models.EmailField(max_length=150,null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,
    related_name='members')

    def __str__(self):
        return self.name + ' | ' + self.department.name + ' | ' + self.position

class UpcomingEvent(models.Model):
    eventTitle = models.CharField(max_length=100)
    date=models.DateField(null=True)
    description=models.CharField(max_length=5000)
    speaker=models.CharField(max_length=100)
    upload = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.eventTitle 

class PastEvent(models.Model):
    title = models.CharField(max_length=100)
    date=models.DateField(null=True)
    eventInfo=models.CharField(max_length=5000)
    # speaker=models.CharField(max_length=100)
    poster = models.ImageField(upload_to ='pastUploads/')
    venue=models.CharField(max_length=100,null=True)

    def __str__(self)->str:
        return self.title 

class PostImage(models.Model):
    post=models.ForeignKey(to=PastEvent,on_delete=models.CASCADE, related_name='post')
    image=models.ImageField(upload_to='pastUploads/')
    
    def __str__(self)->str:
        return self.image.url







