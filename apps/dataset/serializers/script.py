from rest_framework import serializers

from dataset.models import TblScript


class ScriptSerializers(serializers.ModelSerializer):
    class Meta:
        model = TblScript
        fields = '__all__'
        