from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:blog>", views.blog_list_by_number),
    path("<str:blog>", views.blog_list_by_number, name='blog-post'),

]
