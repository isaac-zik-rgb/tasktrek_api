from .models import User
from django.db.models.signals import pre_save, post_save
from .models import Profile
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, phone=instance.phone, country=instance.country, email=instance.email)



@receiver(pre_save, sender=User)
def create_username(sender, instance, **kwargs):
    if not instance.username:
        username = f"{instance.first_name}_{instance.last_name}".lower()
        count = 1
        while User.objects.filter(username=username):
            username = f"{instance.first_name}_{instance.last_name}_{count}".lower()
            count +=1

        instance.username = username
        