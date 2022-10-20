from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

from dataset.serializers import RestSerializers
from dataset.models import TblRest


@extend_schema_view(
    list=extend_schema(summary='获取静态数据'),
    create=extend_schema(summary='创建静态数据'),
    update=extend_schema(summary='更新静态数据'),
    destroy=extend_schema(summary='删除静态数据'),
    retrieve=extend_schema(summary='获取静态数据')
)
class RestViewSet(ModelViewSet):
    queryset = TblRest.objects.all()
    serializer_class = RestSerializers
    authentication_classes = []
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)