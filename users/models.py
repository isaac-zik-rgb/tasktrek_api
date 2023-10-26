
from django.db import models
import os
from django.utils.deconstruct import deconstructible
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=30, blank=False)
    birth_date = models.DateField('Date of birth', null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)

    


@deconstructible
class FileGeneratorPath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        imageext = ['jpg', 'png']
        if ext not in imageext:
            path = f"media/account/{instance.user.id}/files"
            name = f"resume.{ext}"
        else:
            path = f"media/account/{instance.user.id}/images"
            name = f"profile_image.{ext}"

        
        return os.path.join(path, name)

profile_image_path = FileGeneratorPath()
user_resume = FileGeneratorPath()

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('User', related_name='posts', on_delete=models.CASCADE)

    def formatted_created(self):
        return self.created.strftime("%m/%d/%Y %I:%M %p")
    
    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['created']
    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey('User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def formatted_created(self):
        return self.created.strftime("%m/%d/%Y %I:%M %p")


    class Meta:
        ordering = ['created']



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image =models.FileField(upload_to=profile_image_path, null=True, blank=True)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    resume = models.FileField(upload_to=user_resume, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)



    def save(self, *args, **kwargs):
        # Set the profile's id to match the user's id
        self.id = self.user.id
        super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username}'s profile"
    