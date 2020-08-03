from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
  {
    'author': 'Vanna Chan',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'August 3, 2020'
  },
  {
    'author': 'Jane Doe',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'August 4, 2020'
  }
]

# this function will handle traffic from home
def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):

  # return HttpResponse('<h1>Blog About</h1>')
  return render(request, 'blog/about.html', {'title': 'About'})