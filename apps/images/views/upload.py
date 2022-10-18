   
import os
import hashlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status as HttpStatus
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema

from images.models import TblImage
from images.serializers.image import UploadImageSerializers
from utils.qiniu import upload_image


class ImageUploadView(APIView):
    parser_classes = [MultiPartParser]
    
    @extend_schema(
        summary='上传图片',
        request=UploadImageSerializers
    )
    def post(self, request):
        file_obj = request.data.get('file') 
        if not file_obj:
            return Response('The correct file was not sent', status=HttpStatus.HTTP_406_NOT_ACCEPTABLE)
        
        # 如果不是文件，就直接保存处理
        content = b''
        for chunk in file_obj.chunks():
            content += chunk
        
        ret = self.save_file(content, file_obj.name)
        if ret:
            return Response({'url': f'{settings.QINIU_URL}{ret["key"]}'})
        else:
            return Response(status=HttpStatus.HTTP_400_BAD_REQUEST)
    
    def save_file(self, content: bytes, name: str):
        md5 = hashlib.md5(content).hexdigest()
        filename = f'{md5}_{name}'
        
        TblImage.objects.update_or_create(md5=md5, defaults={
            "name": name,
            "md5": md5, 
            "url": f'{settings.QINIU_URL}{settings.IMAGE_FLODER}{filename}'
            })
        return upload_image(f'{settings.IMAGE_FLODER}{filename}', content)
        
    @extend_schema(
        summary='导出图片'
    )
    def get(self, request: Request):
        file_path = Path(settings.MEDIA_ROOT)
        group_path = Path(settings.FILE_DIR).absolute()
        group_file = group_path.joinpath('images.zip')
        if group_file.exists():
            os.remove(group_file)
        with ZipFile(group_file, 'w', ZIP_DEFLATED) as myzip:
            for item in file_path.iterdir():
                myzip.write(item,item.name)
        return  Response(f'{settings.FILE_URL}images.zip')

