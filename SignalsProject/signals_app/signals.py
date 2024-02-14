

from django.db.models.signals import post_save,pre_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
 

 


          
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
  
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
        instance.profile.save()

@receiver(pre_save, sender=User) 
def checker(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
      current=instance
      previous=User.objects.get(id=instance.id)
      if previous.reaction!= current.reaction:
          pass