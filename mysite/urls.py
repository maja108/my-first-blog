#from django.conf.urls import url
##from . import views
#from django.shortcuts import render

# Create your views here.
#urlpatterns = [
#    url(r'^$', views.post_list, name='post_list'),
#]


from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]