import json
import tempfile
from pathlib import Path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status as HttpStatus
from drf_spectacular.utils import extend_schema

from page.serializers import FilePageSerializers
from page.models import TblPage
from utils.utils import decompress_zip


class UploadPageView(APIView):
    authentication_classes = []
    parser_classes = [MultiPartParser]
    
    @extend_schema(
        request=FilePageSerializers,
        summary='上传页面文件'
    )
    def post(self, request):
        group = request.query_params.get('group','default')
        file_obj = request.data['file']
        if file_obj.name.split('.')[-1] not in ['json', 'zip']:
            return Response('The file format must be .json/.zip', status=HttpStatus.HTTP_406_NOT_ACCEPTABLE)
        
        import_finish = False
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpfilename = Path(tmpdirname).joinpath(file_obj.name)
            with open(tmpfilename, 'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
                    
            if 'zip' in tmpfilename.suffix:
                decompress_zip(str(tmpfilename), tmpdirname)
            
            
            for fileobj in Path(tmpdirname).glob('**/*.json'):
                import_finish = False
                item = json.loads(fileobj.read_text(encoding='utf-8'))
                page = TblPage(id=item.get('id'), name=item['name'], canvas_data=item['canvasData'], canvas_style=item['canvasStyle'], is_home=item.get('is_home', False), group=group)
                page.save()
                import_finish = True
                
        # shutil.rmtree(tmpdirname)
        if import_finish:
            return Response('Import success')

        return Response('Import failure', status=HttpStatus.HTTP_400_BAD_REQUEST)