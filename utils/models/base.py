from django.db import models
from django.contrib.auth.backends import UserModel


class BaseModel(models.Model):
    name = models.CharField(max_length=64, help_text='名称')
    remark = models.CharField(max_length=256, blank=True, null=True, help_text='备注')
    author = models.ForeignKey(UserModel, on_delete=models.SET_NULL, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    update_at = models.DateTimeField(auto_now=True, help_text='更新时间')
    is_lock = models.PositiveSmallIntegerField(default=0, help_text='是否锁定')
    
    class Meta:
        abstract = True
