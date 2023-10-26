from django.contrib import admin
from .models import Profile
from .models import User, Post

# Register your models here.
# from authemail.admin import EmailUserAdmin
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Post)

