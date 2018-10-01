from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('game/<int:game_id>', views.game, name="game" )
]