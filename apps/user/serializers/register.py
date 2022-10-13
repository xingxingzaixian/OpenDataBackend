from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class RegisterSerivalizer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(min_length=6, max_length=32)
    confirm = serializers.CharField(min_length=6, max_length=32)

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm'):
            raise ValidationError(detail='密码不一致')

        return attrs