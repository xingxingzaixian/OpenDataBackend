   
import os
import hashlib
import tempfile
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
from utils.utils import decompress_zip


class ImageUploadView(APIView):
    parser_classes = [MultiPartParser]
    
    @extend_schema(
        summary='上传图片'
    )
    def post(self, request):
        file_obj = request.data.get('file') 
        if not file_obj:
            return Response('The correct file was not sent', status=HttpStatus.HTTP_406_NOT_ACCEPTABLE)
        
        if file_obj.name.split('.')[-1] not in settings.UPLOAD_FORMAT: 
            return Response('The file format must be .png/.jpg/.jpeg/.zip', status=HttpStatus.HTTP_406_NOT_ACCEPTABLE)
        
        file_path = Path(settings.MEDIA_ROOT)
        file_path.mkdir(parents=True, exist_ok=True)

        # 如果不是文件，就直接保存处理
        if not file_obj.name.endswith('zip'): 
            content = b''
            for chunk in file_obj.chunks():
                content += chunk
                
            self.save_file(content, file_path, file_obj.name) 
        # 如果是压缩包，就创建临时目录存储，并解压
        elif file_obj.name.endswith('zip'): 
            with tempfile.TemporaryDirectory() as tmpdirname:
                tmpfilename = Path(tmpdirname).joinpath(file_obj.name)

                # 将压缩文件写入临时目录
                with open(tmpfilename, 'wb') as f:
                    for chunk in file_obj.chunks(): 
                        f.write(chunk)
                        
                # 解压压缩文件
                decompress_zip(str(tmpfilename), tmpdirname)
                
                # 解压完成后删除压缩文件
                # os.remove(tmpfilename)
                
                for file in Path(tmpdirname).glob('**/*.*'):
                    if file.suffix in ('.png', '.jpg', '.jpeg'):
                        self.save_file(file.read_bytes(), file_path, file.name)
        
        return Response(f'{file_obj.name} uploaded',status=204)
    
    def save_file(self, content: bytes, file_path: Path, name: str):
        md5 = hashlib.md5(content).hexdigest()
        new_filename = f'{md5}{Path(name).suffix}'
        with open(file_path.joinpath(new_filename), 'wb') as f:
            f.write(content)
        
        TblImage.objects.update_or_create(md5=md5, defaults={
            "name": name,
            "md5": md5, 
            "url": f'/upload/{new_filename}'
            })
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

