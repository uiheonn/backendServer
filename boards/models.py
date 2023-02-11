from django.db import models
from accounts.models import User
from django.contrib.postgres.fields import ArrayField

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    keyword = models.CharField('제목', max_length=100)
    mail = models.TextField('본문')
    created_at = models.DateTimeField('생성시간', auto_now_add=True)
    modified_at = models.DateTimeField('수정시간', auto_now=True)

    class Meta:
        ordering = ["-created_at"]


class Keyword(models.Model):
    key = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    keyword = models.CharField('키워드', max_length=100)
    mail = models.TextField('메일')
    
'''
class Filter(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    filter_author = models.CharField('발신인', max_length=100)
    title = models.CharField('제목', max_length=100)
    keywordlist = ArrayField(models.CharField(max_length=20), blank=True, null=True)
    emaillist = ArrayField(models.CharField(max_length=100), blank=True, null=True)


class Filtering(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    filter_author = models.CharField('발신인', max_length=100)
    title = models.CharField('제목', max_length=100)
    keywordlist = ArrayField(models.CharField(max_length=20), blank=True, null=True)
    emaillist = ArrayField(models.CharField(max_length=100), blank=True, null=True)
'''
