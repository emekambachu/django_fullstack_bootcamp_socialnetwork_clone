# Group urls.py

from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [

    path('',
         views.ListGroups.as_view(),
         name='all'),

    path('create/',
         views.CreateGroup.as_view(),
         name='create'),

    path('posts/in/<str:slug>/',
         views.SingleGroup.as_view(),
         name='detail'),

    path('join/<str:slug>/',
         views.JoinGroup.as_view(),
         name='join'),

    path('leave/<str:slug>/',
         views.LeaveGroup.as_view(),
         name='leave'),

]