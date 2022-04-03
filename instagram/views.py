from multiprocessing import context
from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Comments,Profile
from .forms import UserRegisterForm,NewPostForm,UpdateUserForm,UpdateUserProfileForm
from django.urls import reverse

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    all_users = User.objects.exclude(id=request.user.id)
    current_user = request.user

    

    return render (request, 'all-insta/home.html',{"posts":posts,"all_users":all_users,"current_user":current_user})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request,"registration/registration_form.html",{'form':form})


def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image = current_user
            image.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render (request, 'all-insta/new_post.html', {"form":form})



def profile(request, username):
    images = request.user.images.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user.profile)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm()

    return render(request, 'all-instagram/profile.html', {'user_form':user_form,'profile_form':profile_form,'images':images})

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