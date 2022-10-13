from django.contrib.auth import authenticate
from django.contrib.auth.backends import UserModel
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status as HttpStatus
from drf_spectacular.utils import extend_schema

from user.serializers import LoginSerivalizer

class LoginView(GenericAPIView):
    authentication_classes = []
    # 这里的 serializer_class 将会提供给 API 文档生成
    serializer_class = LoginSerivalizer
    
    @extend_schema(
        responses={200: str},
        summary='登录'
    )
    def post(self, request):
        ser = LoginSerivalizer(data=request.data)
        ser.is_valid(raise_exception=True)

        username = ser.data.get('username')
        password = ser.data.get('password')

        try:
            user = authenticate(request, username=username, password=password)
            return Response(user.token)  # type: ignore
        except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned) as e:
            return Response(status=HttpStatus.HTTP_400_BAD_REQUEST)
        return Response(status=HttpStatus.HTTP_403_FORBIDDEN)
