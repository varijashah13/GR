from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment',views.postComment,name='postComment'),
    path('', views.grHome, name='grHome'),
    path('<str:slug>', views.grPost, name='grPost'),
    
]