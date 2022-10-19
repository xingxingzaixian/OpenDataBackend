from urllib.request import Request
from rest_framework import status as HttpStatus
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema, extend_schema_view

from images.models import TblImage
from images.serializers import ImageSerializers, DelImageSerializers
from utils.auth.permissions import IsSuperUser
from utils.qiniu import delete_qiniu_image


@extend_schema_view(
    list=extend_schema(
        summary='获取图片列表'
    )
)
class ImageListViewset(ListModelMixin, GenericViewSet):
    queryset = TblImage.objects.all()
    serializer_class = ImageSerializers
    
    def get_authenticators(self):
        if self.request and self.request.method and self.request.method == 'GET':
            self.authentication_classes = []
        return super().get_authenticators()
    
    def get_permissions(self):
        # 只有超级管理员有清理临时图片数据的权限
        if self.request and self.request.method and self.request.method == 'DELETE':
            self.permission_classes = [IsSuperUser]
        return super().get_permissions()
    
    @extend_schema(
        request=DelImageSerializers,
        summary='删除图片'
    )
    @action(methods=['POST'], detail=False, url_name='destory', url_path='destory')
    def destroy_img_image(self, request: Request):
        try:
            imagemd5 = request.data.get('imagemd5')  # type: ignore
            image = TblImage.objects.get(md5=imagemd5)
            # 删除七牛云图片
            image.delete()
        except TblImage.DoesNotExist as e:
            return Response(status=HttpStatus.HTTP_400_BAD_REQUEST)
  
        return Response('Deleting a file succeeded')
 
    @extend_schema(
        summary='清理临时图片'
    )
    @action(methods=['DELETE'], detail=False, url_name='clear', url_path='clear')
    def clear_images(self, request: Request):
        queryset = TblImage.objects.filter(is_lock=0)
        for item in queryset:
            delete_qiniu_image(item.md5)
        queryset.delete()
        return Response('Clean up all unlocked images')
