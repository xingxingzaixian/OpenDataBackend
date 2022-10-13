import os
import json
from pathlib import Path
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status as HttpStatus
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from page.models import TblPage
from page.serializers import PageSerializers, SimplePageSerializers
from utils.logger import getLogger
from utils.utils import compress_zip


logger = getLogger('request')

@extend_schema_view(
    list=extend_schema(summary='获取页面列表'),
    create=extend_schema(summary='创建页面'),
    update=extend_schema(summary='更新页面'),
    destroy=extend_schema(summary='删除页面'),
    retrieve=extend_schema(summary='获取页面')
)
class PageViewset(ModelViewSet):
    queryset = TblPage.objects.all()
    serializer_class = PageSerializers
    
    def get_authenticators(self):
        if self.request and self.request.method and self.request.method == 'GET':
            self.authentication_classes = []
        return super().get_authenticators()
    
    def get_serializer_class(self):
        if self.action == 'list':
            print(self.action)
            self.serializer_class = SimplePageSerializers
        return super().get_serializer_class()
    
    @extend_schema(
        summary='获取首页'
    )
    @action(methods=['GET'], detail=False, url_name='homePage', url_path='homePage')
    def get_home_page(self, request):
        queryset = self.get_queryset()
        try:
            obj = queryset.get(is_home=True)
            serializer = self.get_serializer(instance=obj)
            return Response(serializer.data)
        except TblPage.DoesNotExist as e:
            logger.error(e)
        return Response('not found home page', status=HttpStatus.HTTP_404_NOT_FOUND)
    
    @extend_schema(
        parameters=[
            OpenApiParameter(name='group', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, description='导出项目页面')
        ],
        summary='导出项目'
    )
    @action(methods=['GET'], detail=False, url_name='export', url_path='export')
    def export_project(self, request: Request):
        group = request.query_params.get('group')
        try:
            group_path = Path(settings.FILE_DIR).absolute()
            group_path.mkdir(parents=True, exist_ok=True)
            group_file = group_path.joinpath(f'{group}.zip')
            if group_file.exists():
                os.remove(group_file)
        except Exception as e:
            return Response('The file already exists and is in occupation', status=HttpStatus.HTTP_406_NOT_ACCEPTABLE)
            
        file_list = []
        for page in TblPage.objects.filter(group=group).all():
            page_file = group_path.joinpath(f'{page.name}{str(page.id)}.json')
            file_list.append(page_file)
            page_file.write_text(json.dumps({
                'id': str(page.id),
                'is_home': page.is_home,
                'name': page.name,
                'canvasData': page.canvas_data,
                'canvasStyle': page.canvas_style
            }, ensure_ascii=False))
            
        compress_zip(group_file, file_list)
        
        return Response(f'{settings.FILE_URL}{group}.zip')
