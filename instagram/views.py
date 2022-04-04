from multiprocessing import context
from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Comments,Profile
from .forms import UserRegisterForm,NewPostForm,UpdateUserForm,UpdateUserProfileForm
from django.urls import reverse
from django.contrib.auth import authenticate,login
from django.contrib import messages



# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    posts = Image.objects.all()
    all_users = User.objects.exclude(id=request.user.id)
    current_user = request.user

    

    return render (request, 'all-insta/home.html',{"posts":posts,"all_users":all_users,"current_user":current_user})


def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            
            image = form.save()
            image = current_user
            image.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render (request, 'all-insta/new_post.html', {"form":form})



def profile(request):
    

    return render(request, 'all-insta/profile.html', {})

def search_results(request):
     
     if 'profile' in request.GET and request.GET["profile"]:
         search_term = request.GET.get("profile")
         searched_profiles = Profile.search_by_profile(search_term)
         message = f"{search_term}"

         return render (request, 'all-insta/search.html',{"message":message,"profiles":searched_profiles})

     else:
         message = "You haven't searched for any User"
         return render (request, 'all-insta/search.html',{"message":message})

def like(request,id):
    post = Image.objects.get(id = id)
    post.likes +=1
    post.save()
    return HttpResponseRedirect(reverse("home"))