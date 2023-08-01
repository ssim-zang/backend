from django.shortcuts import render
from django.http import HttpResponse
from .apis import member as MemberAPI
from django.shortcuts import redirect

def index(request):
    # if(request.session.get('id')):
    #     request.session['id'] = None
    
    return render(request, "index.html")

def login(request):
    if(request.session.get('id')):
        return redirect('/')
    return render(request, "login.html")

def myPage(request):
    return render(request, "mypage.html")

