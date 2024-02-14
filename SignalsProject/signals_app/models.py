from django.db import models
from django.contrib.auth.models import User,Group
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from PIL import Image


 
class Profile(models.Model):
    """
        establishes a one-to-one relationship with the built-in User model
    """
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
