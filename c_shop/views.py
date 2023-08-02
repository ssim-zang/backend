from django.shortcuts import render
from django.http import HttpResponse
from .apis import member as MemberAPI
from django.shortcuts import redirect, get_object_or_404
from django.core import serializers
from c_shop.models import Member, Board, Company
import random

def index(request):
    # if(request.session.get('id')):
    #     request.session['id'] = None
    
    return render(request, "index.html")

def login(request):
    if(request.session.get('id')):
        return redirect('/')
    return render(request, "login.html")

def myPage(request):
    if(not request.session.get('id')):
        return redirect('/login/')
    user = get_object_or_404(Member, pk=request.session.get('id'))
    myBoard = Board.objects.filter(user=user).count()
    return render(request, "mypage.html", {"data":user,"myBoard":myBoard, "plantExp":user.plantExp%700})

def shop(request):
    data = list(Company.objects.all())
    # data = random.shuffle(data*5)
    return render(request, "shop.html",{"data":data*5})

def project(request):
    return render(request, "project.html")
def projectDetail(request):
    return render(request, "project-detail.html")

def communityEdit(request):
    return render(request, "community/edit.html")
def communityList(request):
    return render(request, "community/list.html")
def communityView(request, id):
    return render(request, "community/view.html")
def communityWrite(request):
    return render(request, "community/write.html")



    