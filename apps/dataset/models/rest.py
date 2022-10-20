from django.db import models

from utils.models import BaseModel


class TblRest(BaseModel):
    method = models.CharField(max_length=10, help_text='请求方法')
    url = models.CharField(max_length=256, help_text='请求地址')
    headers = models.JSONField(help_text='请求头', default=dict)
    params = models.JSONField(help_text='请求参数', default=dict)
    data = models.JSONField(help_text='请求体参数', default=dict)
    
    class Meta:
        db_table = 'tbl_rest'
        verbose_name = 'API数据'
        verbose_name_plural = 'API数据'