from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Tournament(models.Model):
    name = models.CharField('naam', max_length=60, unique=True)
    fields = models.SmallIntegerField('velden', validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'toernooi'
        verbose_name_plural = 'toernooien'


class Team(models.Model):
    name = models.CharField('naam', max_length=60, unique=True)
    tournament = models.ForeignKey(Tournament, models.CASCADE, verbose_name='toernooi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'


class Participant(models.Model):
    first_name = models.CharField('voornaam', max_length=60)
    last_name = models.CharField('achternaam', max_length=100)
    team = models.ForeignKey(Team, models.CASCADE, verbose_name='team')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'deelnemer'
        verbose_name_plural = 'deelnemers'


class Game(models.Model):
    GAME_TYPES = [
        ('group', 'poulefase'),
        ('2nd_group', '1e ronde'),
        ('1_8_final', 'achtste finale'),
        ('1_4_final', 'kwartfinale'),
        ('1_2_final', 'halve finale'),
        ('consolation_final', 'troost finale'),
        ('final', 'finale'),
    ]
    BRACKETS = [
        ('winners', 'winnaars'),
        ('losers', 'verliezers'),
    ]
    home_team = models.ForeignKey(Team, models.PROTECT, related_name='related_home_team', verbose_name='thuis team')
    home_team_score = models.SmallIntegerField('score thuis team', blank=True)
    away_team = models.ForeignKey(Team, models.PROTECT, related_name='related_away_team', verbose_name='uit team')
    away_team_score = models.SmallIntegerField('score uit team', blank=True)
    type = models.CharField('type', max_length=30, choices=GAME_TYPES, default='group')
    round = models.CharField('ronde', max_length=30, choices=BRACKETS, blank=True)
    field = models.PositiveSmallIntegerField('veld', validators=[MinValueValidator(1)])

    def get_result(self):
        if self.home_team_score and self.away_team_score:
            if self.home_team_score == self.away_team_score:
                return 0
            return self.home_team if self.home_team_score > self.away_team_score else self.away_team

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('type') == 'group' and cleaned_data.get('round'):
            raise ValidationError('Er kan geen ronde worden ingesteld aan een wedstrijd in de poulefase')
        if cleaned_data.get('home_team') == cleaned_data.get('away_team'):
            raise ValidationError('Het thuisteam en het uitteam kunnen niet gelijk zijn')

        # if cleaned_data.get('field') > cleaned_data.get('home_team'). VALIDATION FOR MAX FIELD

    def __str__(self):
        return f'{self.home_team.name} vs. {self.away_team.name}'

    class Meta:
        verbose_name = 'wedstrijd'
        verbose_name_plural = 'wedstrijden'
