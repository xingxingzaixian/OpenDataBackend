from django.contrib.auth.backends import UserModel
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from user.serializers import RegisterSerivalizer
from utils.logger import getLogger

logger = getLogger('request')
class RegisterView(GenericAPIView):
    authentication_classes = []
    serializer_class = RegisterSerivalizer

    @extend_schema(
        responses={200: str, 400: None},
        summary='注册'
    )
    def post(self, request):
        ser = RegisterSerivalizer(data=request.data)
        ser.is_valid(raise_exception=True)

        username = ser.data.get('username')
        password = ser.data.get('password')

        try:
            UserModel.objects.get(username=username)
        except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned) as e:
            user = UserModel(username=username)
            user.set_password(password)
            # 我们无需额外激活账号，所以注册是自动激活
            user.is_active = True
            user.save()
            logger.info(f'用户: {username} 注册成功')
            return Response('success')
        else:
            return Response('failure')