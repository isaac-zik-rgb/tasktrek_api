from users.models import User, Profile, Post, Comment, Category
from rest_framework import viewsets, mixins
from rest_framework.viewsets import generics
from rest_framework import permissions
from .serializers import UserRegistrationSerializer, UserProfileSerializer, PostSerializer, CommentSerializer, CategorySerializer
from .permissions import UserOwnerOrGetAndPostOnly, IsUserProfileOwnerOrReadOnly, IsOwnerOrReadOnly, IsOwnerOfPostOrCommentOwner

class UserViewsets(viewsets.ModelViewSet):
    permission_classes = (UserOwnerOrGetAndPostOnly,)
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class UserProfileViewset(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = [IsUserProfileOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer

class PostListViewset(viewsets.ModelViewSet):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailViewset(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    
class CommentListViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsOwnerOfPostOrCommentOwner]

class CategoryListViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetailViewset(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
