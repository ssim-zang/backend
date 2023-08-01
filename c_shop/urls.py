from django.urls import path

from . import views
from .apis import member

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    
    
    path("member/create", member.create, name="memberCreate"),
    path("member/login", member.login, name="memberLogin"),
]