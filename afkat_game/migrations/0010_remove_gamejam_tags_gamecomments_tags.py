# Generated by Django 5.1.7 on 2025-04-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afkat_game', '0009_gamejam_tags_alter_game_game_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamejam',
            name='tags',
        ),
        migrations.AddField(
            model_name='gamecomments',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='Games_tags', to='afkat_game.tags'),
        ),
    ]
