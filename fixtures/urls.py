from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixtures, name='fixtures'),
    path('add_fixture/', views.add_fixture, name='add_fixture'),
    path('manage/', views.manage_fixtures, name='manage_fixtures'),
    path('deletefixture/<int:fixture_id>/', views.delete_fixture, name='delete_fixture'),
    path('editfixture/<int:fixture_id>/', views.edit_fixture, name='edit_fixture'),
]