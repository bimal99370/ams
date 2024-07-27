from django.urls import path
from . import views
from .views import manage_groups



urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('players/export/', views.export_players_to_excel, name='export_players_to_excel'),
    path('player/<int:pk>/', views.player_detail, name='player_detail'),
    path('player/new/', views.player_create, name='player_create'),
    path('player/<int:pk>/edit/', views.player_update, name='player_update'),
    path('player/<int:pk>/delete/', views.player_delete, name='player_delete'),

    path('groups/manage/', manage_groups, name='manage_groups'),

]
