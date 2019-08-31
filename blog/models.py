from django.db import models
from django.urls import reverse

from mdeditor.fields import MDTextField


class Navbarmenu(models.Model):
    name = models.CharField('选项名称', max_length=128)
    url = models.URLField('url')

    class Meta:
        verbose_name = '导航栏菜单选项'
        verbose_name_plural = '导航栏菜单选项'

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=256)
    mail = models.EmailField('邮箱', max_length=256)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('分类名', max_length=128)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签名称', max_length=128)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Comment(models.Model):
    body = models.TextField('评论')
    published_time = models.DateTimeField('发布时间', auto_now_add=True)
    author = models.CharField('评论人名字', max_length=128)
    author_url = models.URLField('评论人url', blank=True)
    author_mail = models.EmailField('评论人邮箱')
    parent_comment = models.ForeignKey('self', verbose_name='上级评论', blank=True, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', verbose_name='评论的文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __str__(self):
        return self.body


class Post(models.Model):
    title = models.CharField('标题', max_length=128)
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='文章标签', blank=True)
    allow_comment = models.BooleanField('允许评论', default=True)
    thumb_url = models.URLField('头图url', blank=True)
    excerpt = models.TextField('摘要', max_length=256, blank=True)
    body = MDTextField('正文')
    password = models.CharField('密码', max_length=256, blank=True)
    published_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    views = models.PositiveIntegerField('浏览量', default=0)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
