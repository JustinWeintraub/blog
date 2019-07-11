from django.db import models
from django.core.cache import cache
from django.utils import timezone
import datetime
from website import settings
from django.contrib.auth.models import User #communications between users and poster

class ChatMessage(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE) #replace on delete with on active
    date_posted=models.DateTimeField(default=timezone.now())
    content=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.author.username}:{self.content}'
# Create your models here.
