# Generated by Django 5.2 on 2025-05-09 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afkat_home', '0006_alter_post_options_post_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
