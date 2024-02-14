from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from PIL import Image


# Create your models here 

# class CustomUser(AbstractUser):
#     profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
class Profile(models.Model):
    """
        establishes a one-to-one relationship with the built-in User model
    """
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
