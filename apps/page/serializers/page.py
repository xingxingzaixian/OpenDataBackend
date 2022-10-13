from rest_framework import serializers

from page.models import TblPage


class PageSerializers(serializers.ModelSerializer):
    class Meta:
        model = TblPage
        fields = '__all__'
        

class SimplePageSerializers(serializers.ModelSerializer):
    class Meta:
        model = TblPage
        fields = ('id', 'name', 'thumbnail', 'is_home', 'create_at')
