from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'mainsite'
urlpatterns = [
	# list_view post url 
    path(r'home', views.home, name='home'),
    path(r'contact', views.contact, name='contact'),
    path(r'archive', views.archive, name='archive'),
    path(r'single', views.single, name='single'),

    # detail_view url for the complete post
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
    # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$'
    # RSS Feeds URL
    #url(r'^feed/$', PostsFeed(), name='post_feed')
    ]
