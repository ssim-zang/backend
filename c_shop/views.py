from django.shortcuts import render
from django.http import HttpResponse
from .apis import member as MemberAPI

def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # context = {"latest_question_list": latest_question_list}
    return render(request, "main/index.html")

def login(request):
    if(request.session['id']):
        return render(request, "main/index.html")
    return render(request, "login.html")



