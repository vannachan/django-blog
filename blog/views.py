from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import Post  # import Post class from models

# Dummy data:
# posts = [
#   {
#     'author': 'Vanna Chan',
#     'title': 'Blog Post 1',
#     'content': 'First post content',
#     'date_posted': 'August 3, 2020'
#   },
#   {
#     'author': 'Jane Doe',
#     'title': 'Blog Post 2',
#     'content': 'Second post content',
#     'date_posted': 'August 4, 2020'
#   }
# ]

# this function will handle traffic from home
def home(request):
  context = {
    'posts': Post.objects.all() # using ORM to grab all Posts from table
  }
  return render(request, 'blog/home.html', context)

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html' # by default, it will look for <app>/<model>_<viewtype>.html
  context_object_name = 'posts' # need to do this because home.html is asking for posts
  ordering = ['-date_posted'] # adding - will do DESC order instead

class PostDetailView(DetailView):
  model = Post

def about(request):
  # return HttpResponse('<h1>Blog About</h1>')
  return render(request, 'blog/about.html', {'title': 'About'})