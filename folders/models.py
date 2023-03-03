from django.db import models
from accounts.models import User
# Create your models here.

class Folder2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    folder_name = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    email_domain = models.CharField(max_length=100)