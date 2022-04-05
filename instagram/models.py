
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='images')
    pub_date = models.DateField(auto_now_add=True)
    caption = models.CharField(max_length=250,blank=True)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.name

    def save_image(self):
        return self.save()
    
    @classmethod
    def delete_image(cls,id):
        return cls.objects.filter(id = id).delete()



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='images/',default='no-image')
    bio = models.TextField(max_length=250,blank=True)
    name = models.CharField(blank=True,max_length=100)

    @classmethod
    def search_by_profile(cls,search_term):
        user = cls.objects.filter(profile_icontains=search_term)
        return user


class Comments(models.Model):
    comment = models.TextField(max_length = 350)
    image = models.ForeignKey(Image,null=True, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True) 
    
    
    class Meta:
        ordering = ["-comment_date"]


    def __str__(self):
        return f'{self.user.name} Image'

class Post(models.Model):
    Post_caption = models.CharField(max_length=310,blank=True)
    Post_image = models.ImageField(upload_to='images/', default = 'no-image')
    pub_date = models.DateField(auto_now_add=True)

    @classmethod
    def display_image(cls):
        posts  = cls.objects.all()
        return posts
    

    def __str__(self):
        return self.Post_image
