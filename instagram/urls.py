from unicodedata import name
from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('^$',views.index,name="home"),
    re_path('^new/image$',views.new_post,name = 'new-post'),
    re_path('search/',views.search_results,name='search_results'),
    re_path('like/<id>',views.like,name='like'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
