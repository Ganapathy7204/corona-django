from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [

    path('', views.index, name='index'),
    path('blogPost', views.blogPost, name='blogPost'),
    path('friendsPost', views.friendsPost, name='friendsPost'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('handleSignup', views.handleSignup, name='handleSignup'),
    path('handleLogin', views.handleLogin, name='handleLogin'),
    path('handlelogout', views.handlelogout, name='handlelogout'),
    path('addpost', views.addpost, name='addpost'),
    path('search', views.search, name='search'),
    
    
]
