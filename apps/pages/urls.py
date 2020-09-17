from django.urls import path
from . import views
from ..team.views import *
#from ..team import forms
from django import forms


urlpatterns = [
    path('', views.PageView.as_view()),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('registration/add', AddRegistrationView.as_view(), name="add_registration"),
    #path('registration/success', views.),
    path('<slug:slug>/', views.PageView.as_view(), name="page"),
]
