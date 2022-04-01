from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile

# Create your views here.
def index(request):
    posts = Image.objects.all()
    all_users = User.objects.exclude(id=request.user.id)
    current_user = request.user

    return render (request, 'all-insta/home.html',{"posts":posts,"all-users":all_users,"current_user":current_user})
