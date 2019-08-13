from django.shortcuts import render, get_object_or_404, redirect #shortcuts to templates
#from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post, Comments
from django.http import HttpResponse
from .forms import CommentForm as Creation
import json
from django.views.generic import (
ListView, DetailView, CreateView, UpdateView,DeleteView
)
from django.http import JsonResponse

'''python3 manage.py startapp blog'''
# Create your views here.
'''posts=[
    {
        'author':'Me',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'July 1st, 2019'
    },
    {
        'author':'Bobby',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'July 0th, 2019'
    },
]'''
def home(request): #unused
    context={
    'posts':Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)
class PostListView(ListView):
    def post(self,request):
        print(request.POST)
        form = Creation(request.POST)
        if (form.is_valid() and request.user.is_authenticated):
            #print(form.author.id)
            form=form.save(commit=False)
            form.author=request.user
            form.post_id=request.POST['post_id']
            saver=Post.objects.get(id=request.POST['post_id'])
            form.save()
            try: #depending on database, one will work
                saver.comments.append(form)
                saver.save()
            except:
                saver=Post.objects.filter(id=request.POST['post_id'])
                temp=[]
                temp.append(form)
                saver.update(comments=temp)
        return redirect('blog-home')
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['comments'] = Comments.objects.all()
        context['form']=Creation()
        return context
    model=Post
    template_name='blog/home.html'#<app>/<model>_<viewtype>.html blog/post_list.html
    context_object_name='posts'
    ordering=['-date_posted'] #newest to oldest
    paginate_by=2

def comment(request):
    if(request.method=="POST"):
        data = request.POST.get("postid", "0")
        commentlist=[]
        for comment in Comments.objects.filter(post_id=data):
            commentlist.append(str(comment.author))
            commentlist.append(str(comment.content))
    return(JsonResponse(commentlist, safe=False))
# Create your views here.

class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'#<app>/<model>_<viewtype>.html blog/post_list.html
    context_object_name='posts'
    paginate_by=5
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #get username from paramteres
        return Post.objects.filter(author=user).order_by('-date_posted')
class PostDetailView(DetailView):
    model=Post
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False
def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title':'About'})
def contact(request):
    return render(request, 'blog/contact.html', {'title':'About'})
'''{% if comments.objects.filter(post_id=post.id) %}
  {% for comment in comments.objects.filter(post_id=post.id) %}
  <p>Temp</p>
  {% endfor %}
{% endif %}'''
