# Generated by Django 5.1.7 on 2025-04-07 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afkat_game', '0007_alter_game_rating_alter_gamerating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='download_count',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
