from django.db import models
from accounts.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    folder_name = models.CharField(max_length=100)
    sender = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    #sender = models.CharField(max_length=100)
    keyword = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    #keyword = models.CharField(max_length=100)
    #email_domain = models.CharField(max_length=100)
    email_domain = ArrayField(models.CharField(max_length=100), blank=True, null=True)