from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from utils.models import BaseModel


class TblScript(BaseModel):
    JAVASCRIPT = 'js'
    PYTHON = 'py'
    LANG_CHOICES = [
        (JAVASCRIPT, 'javascript'),
        (PYTHON, 'python')
    ]
    
    type = models.CharField(max_length=2, choices=LANG_CHOICES, default=PYTHON, help_text='脚本语言')  # type: ignore
    code = models.TextField(help_text='脚本内容')
    is_occupy = models.PositiveIntegerField(default=0, help_text='是否被占用')
    
    def __str__(self):
        return self.type
    
    class Meta:
        db_table = 'tbl_script'
        verbose_name = '脚本数据'
        verbose_name_plural = '脚本数据'