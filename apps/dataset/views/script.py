from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

from dataset.models import TblScript
from dataset.serializers import ScriptSerializers


@extend_schema_view(
    list=extend_schema(summary='获取脚本数据'),
    create=extend_schema(summary='创建脚本数据'),
    update=extend_schema(summary='更新脚本数据'),
    destroy=extend_schema(summary='删除脚本数据'),
    retrieve=extend_schema(summary='获取脚本数据')
)
class ScriptViewSet(ModelViewSet):
    queryset = TblScript.objects.all()
    serializer_class = ScriptSerializers