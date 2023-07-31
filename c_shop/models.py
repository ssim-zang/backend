from django.db import models

class Member(models.Model):
    _id = models.CharField(max_length=200)
    pw = models.CharField(max_length=200)
    github = models.CharField(max_length=200, null=True, default=None)
    isOB = models.BooleanField(default=False)
    currentCoin = models.IntegerField(default = 0)
    sumCoin = models.IntegerField(default = 0)
    
