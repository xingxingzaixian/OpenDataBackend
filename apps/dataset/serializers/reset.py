from rest_framework import serializers

from dataset.models import TblReset

class ResetSerializers(serializers.ModelSerializer):
    createDate = serializers.DateTimeField(source='create_at', read_only=True)
    updateDate = serializers.DateTimeField(source='create_at', read_only=True)
    
    class Meta:
        model = TblReset
        fields = ('id', 'name', 'author', 'method', 'url', 'headers', 'params', 'data', 'createDate', 'updateDate')