# Group urls.py

from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [

    path('', views.ListGroups.as_view(), name='all-groups'),
    path('create-group', views.CreateGroup.as_view(), name='create-group'),
    path('posts/in/<str:slug>/', views.SingleGroup.as_view(), name='group-posts')

]