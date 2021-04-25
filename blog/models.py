from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', ]

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file format.')


class UserProfile(models.Model):
    # ایجاد رابطه یک به یک بین پروفایل کاربر و جدول User
    user = models.OneToOneField(User, verbose_name="نام کاربر", on_delete=models.CASCADE)

    # ایجاد یک تصویر برای کاربر
    avatar = models.FileField("تصویر", upload_to='files/user_avatar/', null=False, blank=False,
                              validators=[validate_file_extension])

    # توضیحات
    description = models.CharField("توضیحات", max_length=512, null=False, blank=False)

    #چون پنل ادمین سفارشی شده دیگر نیازی به override کردن متد زیر نیست
    """def __str__(self):
        return self.user.first_name + " " + self.user.last_name"""


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_cover/', null=False, blank=False,
                             validators=[validate_file_extension])
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # چون پنل ادمین سفارشی شده دیگر نیازی به override کردن متد زیر نیست
    """def __str__(self):
        return self.title"""


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/category_cover/', null=False, blank=False,
                             validators=[validate_file_extension])
    # چون پنل ادمین سفارشی شده دیگر نیازی به override کردن متد زیر نیست
    """def __str__(self):
        return self.title"""
