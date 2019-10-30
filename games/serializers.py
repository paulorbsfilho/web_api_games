from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Game, GameCategory, Score, Player


class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = ('name', 'release_date', 'game_category', 'played',)
        validators = [
            UniqueTogetherValidator(
                queryset=Game.objects.all(),
                fields=('name', 'game_category',)
            )
        ]

    ## validacao de data de lancamento
    # def validate_release_date(self, date):
    #     if date <= timezone.now():
    #         raise serializers.ValidationError("this game cant\'t be deleted. It\'s has been released.")
    #     return date


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameCategory
        fields = ('pk', 'name', 'games',)


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')
    player = serializers.SlugRelatedField(queryset=Player.objects.all(),slug_field='name')

    class Meta:
        model = Score
        fields = ('score', 'score_date', 'game', 'player',)


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('id', 'name', 'gender', 'created', 'scores',)
