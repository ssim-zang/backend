from django.shortcuts import render
from django.http import HttpResponse
from .apis import member as MemberAPI

def index(request):
    return HttpResponse(MemberAPI.a() + "Hello, world.")

