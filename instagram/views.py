from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from .forms import PostForm
from django.urls import reverse

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    all_users = User.objects.exclude(id=request.user.id)
    current_user = request.user

    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))

        else:
            post_form = PostForm

    return render (request, 'all-insta/home.html',{"posts":posts,"post_form":post_form,"all_users":all_users,"current_user":current_user})
