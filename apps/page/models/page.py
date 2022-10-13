import uuid
from django.db import models

from utils.models import BaseModel
from .group import TblPageGroup
        
    
class TblPage(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='唯一键')
    thumbnail = models.CharField(max_length=256, default='http://image.xingxingzaixian.fun/pages/1.png', blank=True, help_text='缩略图')
    is_home = models.PositiveSmallIntegerField(default=0, help_text='是否首页')
    is_delete = models.PositiveSmallIntegerField(default=0, help_text='是否删除')
    is_publish = models.PositiveSmallIntegerField(default=0, help_text='是否发布')
    canvas_data = models.JSONField(help_text='组件数据')
    canvas_style = models.JSONField(help_text='画布数据')
    group = models.ForeignKey(TblPageGroup, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tbl_page'
        verbose_name = '页面'
        verbose_name_plural = '页面'
        