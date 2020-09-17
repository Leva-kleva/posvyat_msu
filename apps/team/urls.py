from django.urls import path
from . import views

urlpatterns = [
    #path('', views.AllTeamView.as_view(), name="teams"),
    path('createuser', views.CreateUser.as_view(), name="createuser"),
]
