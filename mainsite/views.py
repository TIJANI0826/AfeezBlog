from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.models import Post


# Create your views here.

def home(request):
	posts = Post.published.all()
	return render(request,'mainsite/home.html', {'posts': posts})

def contact(request):
	return render(request,'mainsite/contact.html')
def single(request):
	return render(request,'mainsite/single.html')
def archive(request):
	return render(request,'mainsite/archive.html')