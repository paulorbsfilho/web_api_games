from django.contrib import admin

# Register your models here.

from games.models import Game, GameCategory, Score, Player

admin.site.register(Game)
admin.site.register(GameCategory)
admin.site.register(Score)
admin.site.register(Player)
