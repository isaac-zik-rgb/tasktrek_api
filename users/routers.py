from rest_framework import routers

from .viewset import UserViewsets, UserProfileViewset, PostListViewset, PostDetailViewset, CommentListViewset, CommentDetailViewset, CategoryListViewset, CategoryDetailViewset
from .viewset import CategoryDetailViewset
"""
define my custom routers for my viewset
"""

app_name = 'ApiApp'

router = routers.DefaultRouter()
router.register('users', UserViewsets)
router.register('profiles', UserProfileViewset)
router.register('posts', PostListViewset, PostDetailViewset)
router.register('comments', CommentListViewset, CommentDetailViewset)
router.register('categories', CategoryListViewset, CategoryDetailViewset)
