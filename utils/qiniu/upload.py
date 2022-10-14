from django.conf import settings

from qiniu import Auth, put_file

def upload_image(filename: str, key: str):
    qn = Auth(settings.QINIU_AK, settings.QINIU_SK)
    token = qn.upload_token(settings.QINIU_BUCKET, key, 3600)
    ret, info = put_file(token, key, filename, version='v2')
    