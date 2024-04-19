from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixtures, name='fixtures'),
    path('add_fixture/', views.add_fixture, name='add_fixture'),
]