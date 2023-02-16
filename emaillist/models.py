from django.db import models
from accounts.models import User

class EmaillistUser(models.Model):
    #g_user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    g_email = models.CharField(max_length = 64, null = True)
    g_password = models.CharField(max_length = 128, null = True)
    g_key = models.CharField(max_length = 64, null = True)
    n_email = models.CharField(max_length = 64, null = True)
    n_password = models.CharField(max_length = 64, null = True)
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    g_key = models.CharField(max_length = 100, null=True)

    '''