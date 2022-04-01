from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='images')
    pub_date = models.DateField(auto_now_add=True)
    caption = models.CharField(max_length=200,blank=True)



class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='images/',default='no-image')
    bio = models.TextField(max_length=200,blank=True)
    name = models.CharField(blank=True,max_length=100)


