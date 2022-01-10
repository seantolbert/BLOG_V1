from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    # path("posts", views.index, name="index"),
    # path('posts/<int:blog>', views.details_by_number),
    # path('posts/<str:blog>', views.details, name='details')
    path("", views.StartingPageView.as_view(), name='home'),
    path("posts/", views.AllPostsView.as_view(), name='index'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
]
