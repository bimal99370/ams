from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
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

                  path('get_group_players/', views.get_group_players, name='get_group_players'),
                  path('delete_group/<int:group_id>/', views.delete_group, name='delete_group'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
