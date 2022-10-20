# Generated by Django 4.1.2 on 2022-10-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TblImage",
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
                    "md5",
                    models.CharField(help_text="文件MD5值", max_length=64, unique=True),
                ),
                ("url", models.CharField(help_text="文件地址", max_length=256)),
                (
                    "is_lock",
                    models.PositiveSmallIntegerField(default=0, help_text="是否锁定"),
                ),
            ],
            options={
                "verbose_name": "图片",
                "verbose_name_plural": "图片",
                "db_table": "tbl_image",
            },
        ),
    ]