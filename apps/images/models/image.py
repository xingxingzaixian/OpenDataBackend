from django.db import models
from django.utils.html import format_html

from utils.models import BaseModel


class TblImage(BaseModel):
    md5 = models.CharField(max_length=64, unique=True, help_text='文件MD5值')
    url = models.CharField(max_length=256, help_text='文件地址')


    def show_pic(self):
        return format_html(f'<img src="{self.url}">')

    show_pic.short_description="图片"
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tbl_image'
        verbose_name = '图片'
        verbose_name_plural = '图片'
        