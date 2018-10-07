from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('game/create',views.create_game, name="create_game"),
    path('game/<int:game_id>', views.game_by_id, name="game" ),
    path('game/<int:game_id>/edit', views.edit_game, name="edit_game"),
    path('game/<int:game_id>/edit/add_story', views.add_story, name="add_story"),
    path('game/<int:game_id>/edit/story/<int:story_id>', views.edit_story, name='edit_story'),
    path('games/list/all', views.games_list_all, name='games_list_all'),
    path('games/list/mine', views.games_list_mine, name='games_list_mine'),
    path('games/list/played', views.games_list_played, name='games_list_played'),
]
