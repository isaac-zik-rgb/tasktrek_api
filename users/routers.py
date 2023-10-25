from rest_framework import routers

from .viewset import UserViewsets, UserProfileViewset

app_name = 'ApiApp'

router = routers.DefaultRouter()
router.register('users', UserViewsets)
router.register('profiles', UserProfileViewset)