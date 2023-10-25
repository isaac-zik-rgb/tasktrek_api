from users.models import User, Profile
from rest_framework import viewsets, mixins
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from .permissions import UserOwnerOrGetAndPostOnly, IsUserProfileOwnerOrReadOnly

class UserViewsets(viewsets.ModelViewSet):
    permission_classes = (UserOwnerOrGetAndPostOnly,)
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class UserProfileViewset(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = (IsUserProfileOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer