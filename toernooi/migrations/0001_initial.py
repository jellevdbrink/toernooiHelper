# Generated by Django 4.2.5 on 2023-09-12 23:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='naam')),
                ('fields', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='velden')),
            ],
            options={
                'verbose_name': 'toernooi',
                'verbose_name_plural': 'toernooien',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='naam')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toernooi.tournament', verbose_name='toernooi')),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='voornaam')),
                ('last_name', models.CharField(max_length=100, verbose_name='achternaam')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toernooi.team', verbose_name='team')),
            ],
            options={
                'verbose_name': 'deelnemer',
                'verbose_name_plural': 'deelnemers',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_score', models.SmallIntegerField(blank=True, verbose_name='score thuis team')),
                ('away_team_score', models.SmallIntegerField(blank=True, verbose_name='score uit team')),
                ('type', models.CharField(choices=[('group', 'poulefase'), ('2nd_group', '1e ronde'), ('1_8_final', 'achtste finale'), ('1_4_final', 'kwartfinale'), ('1_2_final', 'halve finale'), ('consolation_final', 'troost finale'), ('final', 'finale')], default='group', max_length=30, verbose_name='type')),
                ('round', models.CharField(blank=True, choices=[('winners', 'winnaars'), ('losers', 'verliezers')], max_length=30, verbose_name='ronde')),
                ('field', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='veld')),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='related_away_team', to='toernooi.team', verbose_name='uit team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='related_home_team', to='toernooi.team', verbose_name='thuis team')),
            ],
            options={
                'verbose_name': 'wedstrijd',
                'verbose_name_plural': 'wedstrijden',
            },
        ),
    ]
