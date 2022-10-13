from django.db import models

from utils.models import BaseModel


class TblPageGroup(BaseModel):
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tbl_page_group'
        verbose_name = '页面组'
        verbose_name_plural = '页面组'