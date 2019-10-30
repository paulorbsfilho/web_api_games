from django.db import models


class GameCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateTimeField()
    game_category = models.ForeignKey(GameCategory, on_delete=models.CASCADE, related_name='games')
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Player(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=200, blank=True, default='')
    gender = models.CharField(max_length=1, null=False, blank=False, choices=GENDER_CHOICES, default='M')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Score(models.Model):
    score = models.IntegerField()
    score_date = models.DateTimeField()
    game = models.ForeignKey(Game, null=False, blank=False, on_delete=models.CASCADE, related_name='score')
    player = models.ForeignKey(Player, null=False, blank=False, on_delete=models.CASCADE, related_name='scores')

    class Meta:
        ordering = ('-score',)
