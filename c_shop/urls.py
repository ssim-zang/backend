from django.urls import path

from . import views
from .apis import member

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("mypage", views.myPage, name="myPage"),
    path("project", views.project, name="project"),
    path("project/detail", views.projectDetail, name="projectDetail"),
    path("shop", views.shop, name="shop"),
    
    path("community/edit", views.communityEdit, name="communityEdit"),
    path("community/list", views.communityList, name="communityList"),
    path("community/view/<int:id>", views.communityView, name="communityView"),
    path("community/write", views.communityWrite, name="communityWrite"),
    
    
    path("member/create", member.create, name="memberCreate"),
    path("member/login", member.login, name="memberLogin"),
    path("member/logout", member.logout, name="memberLogout"),
    path("member/update", member.update, name="memberUpdate"),
    
    
]