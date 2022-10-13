from django.contrib.auth.backends import UserModel
from rest_framework.viewsets import ModelViewSet

from user.serializers import UserSerializers


class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers