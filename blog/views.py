from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# this function will handle traffic from home
def home(request):
  return render(request, 'blog/home.html')

def about(request):
  # return HttpResponse('<h1>Blog About</h1>')
  return render(request, 'blog/about.html')