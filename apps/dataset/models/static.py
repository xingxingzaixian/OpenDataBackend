from django.db import models

from utils.models import BaseModel


class TblStatic(BaseModel):
    data = models.JSONField(help_text='数据')
    script = models.ForeignKey('TblScript', on_delete=models.CASCADE, null=True, blank=True, help_text='脚本')
    
    class Meta:
        db_table = 'tbl_static'
        verbose_name = '静态数据'
        verbose_name_plural = '静态数据'