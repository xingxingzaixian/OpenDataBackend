from rest_framework.viewsets import ModelViewSet

from dataset.models import TblStatic
from dataset.serializers import StaticSerializers, SimpleStaticSerializers


class StaticViewSet(ModelViewSet):
    queryset = TblStatic.objects.all()
    serializer_class = StaticSerializers
    authentication_classes = []

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = SimpleStaticSerializers
        return super().get_serializer_class()