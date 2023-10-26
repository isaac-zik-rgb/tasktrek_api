from rest_framework import routers

from .viewset import UserViewsets, UserProfileViewset, PostListViewset, PostDetailViewset, CommentListViewset, CommentDetailViewset

app_name = 'ApiApp'

router = routers.DefaultRouter()
router.register('users', UserViewsets)
router.register('profiles', UserProfileViewset)
router.register('posts', PostListViewset)
router.register('posts/<int:pk>', PostDetailViewset)

router.register('comments', CommentListViewset)
router.register('comments/<int:pk>', CommentDetailViewset)