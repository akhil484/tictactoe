from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_board, name="show_board"),
    path("restart", views.restart, name="restart"),
]