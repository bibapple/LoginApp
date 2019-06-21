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
    has_confirmed = models.BooleanField(verbose_name="是否确认", default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmEmail(models.Model):
    code = models.CharField(verbose_name="确认码", max_length=256)
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    c_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.user.name + ":  " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"


