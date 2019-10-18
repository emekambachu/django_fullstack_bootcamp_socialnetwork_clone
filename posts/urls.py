from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [

    path('',
         views.PostList.as_view(),
         name='all-posts'),

    path('create/',
         views.CreatePost.as_view(),
         name='create'),

    path('by/<str:username>/',
         views.UserPosts.as_view(),
         name='for_user'),

    # path('by/<str:username>/<int:pk>/',
    #      views.PostDetail.as_view(),
    #      name='single'),

    path('by/<int:pk>/',
         views.PostDetail.as_view(),
         name='single'),

    path('delete-post/<int:pk>/',
         views.DeletePost.as_view(),
         name='delete-post')

]