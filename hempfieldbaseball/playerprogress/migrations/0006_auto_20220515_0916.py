# Generated by Django 3.2.12 on 2022-05-15 13:16

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('playerprogress', '0005_auto_20210925_1356'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bodyweightimprovement',
            managers=[
                ('leaderboard_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='velocitytype',
            managers=[
                ('leaderboard_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]