from django.urls import path
from . import views

urlpatterns = [
    path('', views.TableView.as_view(), name="table"),
    path('update/table/kek', views.UpdateScore.as_view(), name="rait"),
]
