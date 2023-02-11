from django.db import models
from accounts.models import User
#from django.contrib.postgres.fields import ArrayField
    
class Filter(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    filter_author = models.CharField('발신인', max_length=100)
    title = models.CharField('제목', max_length=100)
    #keywordlist = ArrayField(models.CharField(max_length=20), blank=True, null=True)
    #emaillist = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    keywordlist = models.CharField(max_length=100)
    emaillist = models.CharField(max_length=100)