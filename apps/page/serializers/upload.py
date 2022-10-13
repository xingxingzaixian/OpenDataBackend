from rest_framework import serializers


class FilePageSerializers(serializers.Serializer):
    file = serializers.FileField()