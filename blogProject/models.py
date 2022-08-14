from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='کاربر')
    avatar = models.FileField(upload_to='files/user_avatar/', null=False, blank=False, validators=[validate_file_extension],verbose_name='عکس')
    description = models.CharField(max_length=512, null=False, blank=False,verbose_name='درباره من')
    class Meta:
        verbose_name = 'اطلاعات کاربر'
        verbose_name_plural = 'اطلاعات کاربران'
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False,verbose_name='عنوان')
    cover = models.FileField(upload_to='files/article_cover/', null=False, blank=False, validators=[validate_file_extension],verbose_name='عکس')
    content = RichTextField(verbose_name='محتوا')
    created_at = models.DateTimeField(default=datetime.now, blank=False,verbose_name='تاریخ ایجاد')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,verbose_name='دسته بندی')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name='نویسنده')
    promote = models.BooleanField(default=False,verbose_name='ویژه')
    class Meta:
        verbose_name = 'مقاله '
        verbose_name_plural = 'مقالات'


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False,verbose_name='عنوان')
    cover = models.FileField(upload_to='files/category_cover/', null=False, blank=False, validators=[validate_file_extension],verbose_name='عکس')

    class Meta:
        verbose_name = 'دسته بند'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

