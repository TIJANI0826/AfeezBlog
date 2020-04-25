from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.views.generic.edit import FormView


# Create your views here.
def post_list_view(request):
	list_objects = Post.published.all()
	paginator = Paginator(list_objects,3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,'blog/post/list.html',{'posts': posts})


def post_detail_view(request,year,month,day,post):
	post =get_object_or_404(Post, slug = post, status = 'published',publish__year = year,publish__month = month, publish__day = day)
	return render(request,'blog/post/detail.html',{'post':post})

def edit (post):
	pass

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:post_list_view')

class PostSite(FormView):
    template_name = 'create.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list_view')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
