from django.db import models
from accounts.models import User

class KeywordUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    keyword = models.CharField(max_length=100)