from rest_framework import serializers

class LoginSerivalizer(serializers.Serializer):
    username = serializers.CharField(max_length=64,)
    password = serializers.CharField(min_length=6, max_length=32)
