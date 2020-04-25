from django.conf.urls import url,include
from django.urls import path
from . import views
from .feeds import PostsFeed

app_name = 'blog'
urlpatterns = [
	# list_view post url 
    url(r'^$', views.post_list_view, name='post_list_view'),
    # create your post
    url('^create/$', views.PostCreate.as_view(), name='contact_create'),
    url(r'^create_another', views.PostSite.as_view(),name='create_another'),
    # url('^post_list', views.PostList.as_view(), name='post_list'),

    # detail_view url for the complete post
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
    # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$'
    # RSS Feeds URL
    url(r'^feed/$', PostsFeed(), name='post_feed')
    ]