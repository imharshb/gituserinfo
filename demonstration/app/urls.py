from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('test/', views.test, name = 'test'),
    path('profile/', views.profile, name = 'profile'),
    path('<str:login>/repos/', views.repos, name = 'repos'),
    path('<str:login>/followers/', views.followers, name='followers'),
    path('<str:login>/following/', views.following, name='following'),
    path('<str:login>/repos/<str:value>/', views.branches, name = 'branches'),
    path('<str:login>/repos/<str:value>/commits/', views.commits, name = 'commits'),
]