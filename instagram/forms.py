from django import forms
from django.contrib.auth.models import User
from .models import Image,Profile,Post
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserCreationForm

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Post_image',)


class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    
    # specify model it will interact with
    class Meta:
        model = User  
        fields= ['username','email', 'password1','password2']
        
        help_texts = { 'username': None, 'password2': None, }


User._meta.get_field('email')._unique = True 

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']
        widgets = {
            'bio': Textarea(attrs={'cols': 20, 'rows': 5}),
        }
        
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=300)

    class Meta:
        model = User
        fields = ('username', 'email')
