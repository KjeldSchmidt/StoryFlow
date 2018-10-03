from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('game/create',views.create_game, name="create_game"),
    path('game/<int:game_id>', views.game_by_id, name="game" )
]