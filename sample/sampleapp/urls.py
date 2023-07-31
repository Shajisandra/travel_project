from . import views
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
urlpatterns = [
    path('',views.demo,name="demo"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout")
]