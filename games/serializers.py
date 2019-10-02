import datetime

from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')
        validators = [
            UniqueTogetherValidator(
                queryset=Game.objects.all(),
                fields=('name', 'game_category')
            )
        ]

    def validate_release_date(self, date):
        if date <= timezone.now():
            raise serializers.ValidationError("this game cant\'t be deleted. It\'s has been released.")
        return date
