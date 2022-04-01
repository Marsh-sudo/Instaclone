from django.urls import re_path
from . import views
from django.conf import settings

urlpatterns = [
    re_path('^$',views.index,name="home"),
]