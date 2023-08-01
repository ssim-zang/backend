from django.db import models

class Member(models.Model):
    _id = models.CharField(max_length=200, primary_key=True)
    pw = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    github = models.CharField(max_length=200, null=True, default=None)
    isOB = models.BooleanField(default=False)
    currentCoin = models.IntegerField(default = 0)
    sumCoin = models.IntegerField(default = 0)
    
class Plant(models.Model):
    name = models.TextField(default="애랑이")
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    exp = models.IntegerField(default = 0)
    rebirth = models.IntegerField(default = 0)


class Board(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.TextField(default="")
    content = models.TextField(default="")
    category = models.IntegerField()
    link = models.CharField(max_length=400)
    anonymous = models.BooleanField(default=False)
    
    
class BoardLike(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    
class BoardImages(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="board", null=True)
    
    
class Company(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE) # 해당 기업을 재화로 산 사람
    summary = models.TextField(default="")
    content = models.TextField(default="")
    category = models.TextField(default="")
    images = models.TextField(default="")
    
