from rest_framework import serializers

from user.models import UserInfo

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('username', 'nickname', 'avatar', 'description', 'telephone')