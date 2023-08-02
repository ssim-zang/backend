from django.db import models

class Member(models.Model):
    _id = models.CharField(max_length=200, primary_key=True)
    pw = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    github = models.CharField(max_length=200, default="")
    isOB = models.BooleanField(default=False)
    currentCoin = models.IntegerField(default = 0)
    sumCoin = models.IntegerField(default = 0)
    email = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=200, default="")
    postalCode = models.TextField(max_length=200, default="")
    aboutMe = models.TextField(max_length=200, default="")
    plantName = models.TextField(default="애랑이")
    plantExp = models.IntegerField(default = 0)
    plantRebirth = models.IntegerField(default = 0)
    

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
    obName = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    summary = models.TextField(default="")
    effect = models.TextField(default="")
    price = models.TextField(default="")
    logoImages = models.TextField(default="")
    backgroundImages = models.TextField(default="")
    
