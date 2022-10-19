from django.db import models

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
    
    def __str__(self):
        return self.type
    
    class Meta:
        db_table = 'tbl_script'
        verbose_name = '脚本数据'
        verbose_name_plural = '脚本数据'