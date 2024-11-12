from django.contrib import admin
from django.urls import path
from app.views import CreateUser, LoginUser, RetrieveUser, UpdateUser, DestroyUser
from app.post import CreatePost, RetrievePost, UpdatePost, DestroyPost, RetrieveUserPost, LikePost, CommentPost, \
    FollowUser

urlpatterns = [

    path('user/create/', CreateUser.as_view()),
    path('user/login/', LoginUser.as_view()),
    path('user/<int:pk>/', RetrieveUser.as_view()),
    path('user/update/', UpdateUser.as_view()),
    path('user/delete/<int:pk>/', DestroyUser.as_view()),

    path("post/create/", CreatePost.as_view()),
    path("post/<int:pk>/", RetrievePost.as_view()),
    # path("post/<int:pk>/", RetrievePost.as_view()),
    path("post/update/<int:pk>/", UpdatePost.as_view()),
    path("post/delete/<int:pk>/", DestroyPost.as_view()),

    path('posts/', RetrieveUserPost.as_view()),

    path('post/like/<int:pk>/', LikePost.as_view()),

    path('post/comment/<int:pk>/', CommentPost.as_view()),

    path('user/follow/<int:pk>/', FollowUser.as_view()),

]
