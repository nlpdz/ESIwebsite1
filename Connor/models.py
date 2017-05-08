# from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length = 32)
    pwd = models.CharField(max_length = 32)

class EsiDissertation(models.Model):
    index = models.CharField(max_length = 10, null=True)
    title = models.CharField(max_length = 500, null=True)
    author = models.CharField(max_length = 500, null=True)
    context = models.TextField(max_length = 500, null=True)
    publication = models.CharField(max_length = 255, null=True)