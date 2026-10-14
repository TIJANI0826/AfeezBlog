from django.urls import path, re_path
from . import views
from .feeds import PostsFeed

app_name = 'blog'
urlpatterns = [
    # list_view post url
    re_path(r'^$', views.post_list_view, name='post_list_view'),
    # create your post
    path('create/', views.PostCreate.as_view(), name='contact_create'),
    re_path(r'^create_another', views.PostSite.as_view(),name='create_another'),
    # url('^post_list', views.PostList.as_view(), name='post_list'),

    # detail_view url for the complete post
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
    # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$'
    # RSS Feeds URL
    re_path(r'^feed/$', PostsFeed(), name='post_feed')
    ]
