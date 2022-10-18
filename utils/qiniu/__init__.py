from django.conf import settings

from qiniu import Auth, BucketManager, put_data

def upload_image(filename, content, time_out=3600):
    request = Auth(settings.QINIU_AK, settings.QINIU_SK)
    token = request.upload_token(settings.QINIU_BUCKET, filename, time_out)
    ret, _ = put_data(token, filename, content)
    return ret


def delete_qiniu_image(key):
    request = Auth(settings.QINIU_AK, settings.QINIU_SK)
    bucket = BucketManager(request)
    ret, _ = bucket.delete(settings.QINIU_BUCKET, key)
    return ret
    