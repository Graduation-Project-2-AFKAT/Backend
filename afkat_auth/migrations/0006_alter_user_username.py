# Generated by Django 5.2b1 on 2025-03-11 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afkat_auth', '0005_user_github_link_user_linkedin_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='Username'),
        ),
    ]
