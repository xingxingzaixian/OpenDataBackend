from rest_framework import serializers

from dataset.models import TblStatic

class StaticSerializers(serializers.ModelSerializer):
    createDate = serializers.DateTimeField(source='create_at', read_only=True)
    updateDate = serializers.DateTimeField(source='create_at', read_only=True)
    
    class Meta:
        model = TblStatic
        fields = ('id', 'name', 'author', 'data', 'createDate', 'updateDate')
        

class SimpleStaticSerializers(serializers.ModelSerializer):
    class Meta:
        model = TblStatic
        fields = ('id', 'name', 'author')