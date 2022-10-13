from rest_framework import serializers
from page.models import TblPageGroup


class PageGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = TblPageGroup
        fields = '__all__'