from django.db import models
from accounts.models import User

class Emaillist2User(models.Model):
    #g_user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    g_key = models.CharField(max_length = 100, null=True)
    
