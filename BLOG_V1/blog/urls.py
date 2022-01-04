from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    # path("posts", views.index, name="index"),
    # path('posts/<int:blog>', views.details_by_number),
    # path('posts/<str:blog>', views.details, name='details')
    path("", views.home, name='home'),
    path('posts', views.posts, name='posts'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail') #/poosts/my-first-post
]
