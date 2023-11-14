from .models import User
from django.db.models.signals import pre_save, post_save
from .models import Profile
from django.dispatch import receiver

# a function that create the user profile when the user is creatd with some data
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, phone=instance.phone, country=instance.country, email=instance.email)




        
