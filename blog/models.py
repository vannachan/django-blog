from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100) # title a field of Post table
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now) # we are passing in the function but we are not executing the function, hence no timezone.now()
  author = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted, delete the post too

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})


