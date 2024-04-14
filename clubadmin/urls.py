from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_admin, name='club_admin'),
]