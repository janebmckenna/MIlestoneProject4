from django.urls import path
from . import views


urlpatterns = [
    path('', views.subs, name='subs'),
    path('all_subs/', views.all_subs, name='all_subs'),
    path('add_subs/', views.add_subs, name='add_subs'),
]
