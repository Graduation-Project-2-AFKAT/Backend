# Generated by Django 5.1.7 on 2025-04-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afkat_game', '0013_remove_gamejam_contest_id_gamejam_game_jam_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamejam',
            name='game_jam_thumbnail',
            field=models.ImageField(blank=True, default='default_images/default_game.jpg', upload_to='game_jams/thumbnails/'),
        ),
    ]
