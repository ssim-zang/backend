from django.urls import path

from . import views
from .apis import member

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("mypage", views.myPage, name="myPage"),
    path("project", views.project, name="project"),
    path("shop", views.shop, name="shop"),
    
    
    path("member/create", member.create, name="memberCreate"),
    path("member/login", member.login, name="memberLogin"),
    path("member/logout", member.logout, name="memberLogout"),
]