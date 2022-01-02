from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:blog>', views.details_by_number),
    path('<str:blog>', views.details, name='details')
]
