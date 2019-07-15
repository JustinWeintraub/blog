from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #communications between users and poster
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

class Comments(models.Model):
    content=models.CharField(max_length=100)
    date_posted=models.DateTimeField(default=timezone.now())
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post_id=models.CharField(max_length=1000)
    def __str__(self):
        return(self.content)
class Post(models.Model): #goes off of database of people?
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now())#not a last modified, post creation
    author=models.ForeignKey(User,on_delete=models.CASCADE) #if user is dead delete post
    comments=models.CharField(max_length=1000, editable=False)
    #comments=ArrayField(models.CharField(max_length=100, editable=False),default=[])
    def __str__(self):
        return(self.title)
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk}) #don't have to put in link, reverse goes to area
