from rest_framework import viewsets
from apps.users.permissions import SuperUserAllowAllPermission
from apps.users.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    permission_classes = [SuperUserAllowAllPermission]
