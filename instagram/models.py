
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='images')
    pub_date = models.DateField(auto_now_add=True)
    caption = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.name

    def save_image(self):
        return self.save()
    
    @classmethod
    def delete_image(cls,id):
        return cls.objects.filter(id = id).delete()



class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='images/',default='no-image')
    bio = models.TextField(max_length=200,blank=True)
    name = models.CharField(blank=True,max_length=100)


