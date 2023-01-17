from django.db import models
from accounts.models import User
from rest_framework import serializers
import json

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

class Filter(models.Model):
    #author1 = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    authorr = models.CharField('발신인', max_length=100)
    title = models.CharField('제목', max_length=100)
    keywordlist = models.CharField('키워드리스트', max_length=100)
    emaillist = models.CharField('이메일리스트', max_length=100)
    '''
    def set_title(self, x):
        set_title = json.dump(x)
    '''