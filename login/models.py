from django.db import models


class User(models.Model):
    gender = (
        ("male", "男"),
        ("female", "女")
    )

    name = models.CharField(max_length=128, verbose_name="用户名", unique=True)
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.EmailField(verbose_name="邮箱", unique=True)
    sex = models.CharField(max_length=32, verbose_name="性别", choices=gender, default="男")
    c_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


