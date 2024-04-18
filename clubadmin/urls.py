from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_admin, name='club_admin'),
    path('edit_delete_admin', views.edit_delete_admin, name='edit_delete_admin'),
    path('manage_categories', views.manage_categories, name='manage_categories'),
    path('add_news/', views.add_news, name='add_news'),
    path('edit_delete_news/', views.edit_delete_news, name='edit_delete_news'),
    path('deletenews/<int:news_id>/', views.delete_news, name='delete_news'),
    path('editnews/<int:news_id>/', views.edit_news, name='edit_news'),
    path('news/<int:news_id>/', views.news_item, name='news_item'),
    path('allnews', views.all_news, name='all_news'),
]