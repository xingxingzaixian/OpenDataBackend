from rest_framework import serializers

from images.models import TblImage


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = TblImage
        fields = '__all__'


class DelImageSerializers(serializers.Serializer):
    filemd5 = serializers.CharField(max_length=64, required=True, help_text='文件MD5编码')
    

class UploadImageSerializers(serializers.Serializer):
    file = serializers.ImageField()