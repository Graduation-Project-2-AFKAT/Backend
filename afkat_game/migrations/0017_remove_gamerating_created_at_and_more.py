# Generated by Django 5.1.7 on 2025-04-13 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afkat_game', '0016_gamejam_submitted_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamerating',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='gamerating',
            name='updated_at',
        ),
    ]
