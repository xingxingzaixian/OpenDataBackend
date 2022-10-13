from rest_framework.viewsets import ModelViewSet

from page.models import TblPageGroup
from page.serializers import PageGroupSerializers


class PageGroupViewset(ModelViewSet):
    queryset = TblPageGroup.objects.all()
    serializer_class = PageGroupSerializers
    