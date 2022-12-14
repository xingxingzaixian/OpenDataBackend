from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

from dataset.models import TblStatic
from dataset.serializers import StaticSerializers, SimpleStaticSerializers


@extend_schema_view(
    list=extend_schema(summary='获取静态数据'),
    create=extend_schema(summary='创建静态数据'),
    update=extend_schema(summary='更新静态数据'),
    destroy=extend_schema(summary='删除静态数据'),
    retrieve=extend_schema(summary='获取静态数据')
)
class StaticViewSet(ModelViewSet):
    queryset = TblStatic.objects.all()
    serializer_class = StaticSerializers
    authentication_classes = []

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = SimpleStaticSerializers
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)