# Generated by Django 4.1.2 on 2022-10-20 10:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TblPage",
            fields=[
                ("name", models.CharField(help_text="名称", max_length=64)),
                (
                    "remark",
                    models.CharField(
                        blank=True, help_text="备注", max_length=256, null=True
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, help_text="创建时间"),
                ),
                ("update_at", models.DateTimeField(auto_now=True, help_text="更新时间")),
                (
                    "is_lock",
                    models.PositiveSmallIntegerField(default=0, help_text="是否锁定"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="唯一键",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "thumbnail",
                    models.CharField(
                        blank=True,
                        default="http://image.xingxingzaixian.fun/pages/1.png",
                        help_text="缩略图",
                        max_length=256,
                    ),
                ),
                (
                    "is_home",
                    models.PositiveSmallIntegerField(default=0, help_text="是否首页"),
                ),
                (
                    "is_delete",
                    models.PositiveSmallIntegerField(default=0, help_text="是否删除"),
                ),
                (
                    "is_publish",
                    models.PositiveSmallIntegerField(default=0, help_text="是否发布"),
                ),
                ("canvas_data", models.JSONField(help_text="组件数据")),
                ("canvas_style", models.JSONField(help_text="画布数据")),
            ],
            options={
                "verbose_name": "页面",
                "verbose_name_plural": "页面",
                "db_table": "tbl_page",
            },
        ),
        migrations.CreateModel(
            name="TblPageGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(help_text="名称", max_length=64)),
                (
                    "remark",
                    models.CharField(
                        blank=True, help_text="备注", max_length=256, null=True
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, help_text="创建时间"),
                ),
                ("update_at", models.DateTimeField(auto_now=True, help_text="更新时间")),
                (
                    "is_lock",
                    models.PositiveSmallIntegerField(default=0, help_text="是否锁定"),
                ),
            ],
            options={
                "verbose_name": "页面组",
                "verbose_name_plural": "页面组",
                "db_table": "tbl_page_group",
            },
        ),
    ]
