from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.cache import cache
import datetime
from website import settings

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save() #saving parent class
        try:
            img=Image.open(self.image.path)
            if(img.height>300 or img.width>300):
                output_size=(300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        except:
            pass
    def last_seen(self):
        return cache.get('seen_%s' % self.user.username)
    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            print(now-self.last_seen())
            if now > self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False

#python3 manage.py makemigrations , migrate, done to update database with new info
