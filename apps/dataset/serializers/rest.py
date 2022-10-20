from rest_framework import serializers

from dataset.models import TblRest

class RestSerializers(serializers.ModelSerializer):
    createDate = serializers.DateTimeField(source='create_at', read_only=True)
    updateDate = serializers.DateTimeField(source='create_at', read_only=True)
    
    class Meta:
        model = TblRest
        fields = ('id', 'name', 'author', 'method', 'url', 'headers', 'params', 'data', 'createDate', 'updateDate')
        
        
class SingleRestSerializers(serializers.ModelSerializer):
    createDate = serializers.DateTimeField(source='create_at', read_only=True)
    updateDate = serializers.DateTimeField(source='create_at', read_only=True)
    
    class Meta:
        model = TblRest
        fields = '__all__'