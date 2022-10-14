from rest_framework import serializers

from page.models import TblPage


class PageSerializers(serializers.ModelSerializer):
    isHome = serializers.IntegerField(source='is_home', default=0)
    isDelete = serializers.IntegerField(source='is_delete', default=0)
    isPublish = serializers.IntegerField(source='is_publish', default=0)
    canvasData = serializers.JSONField(source='canvas_data')
    canvasStyle = serializers.JSONField(source='canvas_style')
    createTime = serializers.DateTimeField(source='create_at', read_only=True)
    
    class Meta:
        model = TblPage
        fields = ('id', 'name', 'thumbnail', 'author', 'isHome', 'isDelete', 'isPublish', 'canvasData', 'canvasStyle', 'createTime')
        

class SimplePageSerializers(serializers.ModelSerializer):
    isHome = serializers.IntegerField(source='is_home', default=0)
    createTime = serializers.DateTimeField(source='create_at', read_only=True)
    
    class Meta:
        model = TblPage
        fields = ('id', 'name', 'thumbnail', 'isHome', 'createTime')
