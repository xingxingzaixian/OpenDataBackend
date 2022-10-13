from django.contrib.auth.models import AbstractUser
from django.db import models


class UserInfo(AbstractUser):
    nickname = models.CharField(max_length=64, help_text='昵称')
    avatar = models.CharField(max_length=256, null=True, blank=True, help_text='头像')
    description = models.CharField(max_length=256, null=True, blank=True, help_text='自我介绍')
    telephone = models.CharField(max_length=11, blank=True, null=True, help_text='手机号码')
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    update_at = models.DateTimeField(auto_now=True, help_text='创建时间')
  
    def __str__(self):
        return self.username
      
    class Meta:
        db_table = 'tbl_user'
        verbose_name = '用户表'
        verbose_name_plural = '用户表'