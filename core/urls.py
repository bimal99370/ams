from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core import views


urlpatterns = [
                  path('', views.player_list, name='player_list'),
                  path('players/export/', views.export_players_to_excel, name='export_players_to_excel'),
                  path('player/<int:pk>/', views.player_detail, name='player_detail'),
                  path('player/new/', views.player_create, name='player_create'),
                  path('player/<int:pk>/edit/', views.player_update, name='player_update'),
                  path('player/<int:pk>/delete/', views.player_delete, name='player_delete'),
                  path('groups/manage/', views.manage_groups, name='manage_groups'),

                  path('get_group_players/', views.get_group_players, name='get_group_players'),
                  path('delete_group/<int:group_id>/', views.delete_group, name='delete_group'),

                  path("upload/", views.upload_file, name="upload_file"),
                  path('download-blank-excel/', views.download_blank_excel, name='download_blank_excel'),

                  path('groups/', views.manage_all_groups, name='manage_all_groups'),
                  path('get_all_players/', views.get_all_players, name='get_all_players'),

                  path('update_group/',views.update_group, name='update_group'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
