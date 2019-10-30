from django.urls import path
from games import views

urlpatterns = [
        path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
        path('games/', views.GameList.as_view(), name=views.GameList.name),
        path('games/<int:id>', views.GameDetail.as_view(), name=views.GameDetail.name),
        path('game-categories/', views.GameCategoryList.as_view(), name=views.GameCategoryList.name),
        path('game-categories/<int:id>', views.GameCategoryList.as_view(), name=views.GameCategoryList.name),
        path('players/', views.PlayerList.as_view(), name=views.PlayerList.name),
        path('players/<int:id>', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
        path('scores/', views.ScoreList.as_view(), name=views.ScoreList.name),
        path('scores/<int:id>', views.ScoreDetail.as_view(), name=views.ScoreDetail.name),
    ]