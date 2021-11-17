from rest_framework.generics import RetrieveAPIView
from api.v1 import permissions
from api.v1.user import serializers
from user.models import User


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorePermission
    ]
