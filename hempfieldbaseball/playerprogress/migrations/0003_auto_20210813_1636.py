# Generated by Django 3.2.3 on 2021-08-13 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerprogress', '0002_auto_20210613_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distanceimprovement',
            options={'ordering': ['-player__graduation_year', 'ttype__name'], 'verbose_name': 'Distance Improvement', 'verbose_name_plural': 'Distance Improvements'},
        ),
        migrations.AlterModelOptions(
            name='liftimprovement',
            options={'ordering': ['-player__graduation_year', 'ttype__name'], 'verbose_name': 'Lift Improvement', 'verbose_name_plural': 'Lift Improvements'},
        ),
        migrations.AlterModelOptions(
            name='timeimprovement',
            options={'ordering': ['-player__graduation_year', 'ttype__name'], 'verbose_name': 'Time Improvement', 'verbose_name_plural': 'Time Improvements'},
        ),
        migrations.AlterModelOptions(
            name='velocityimprovement',
            options={'ordering': ['-player__graduation_year', 'ttype__name'], 'verbose_name': 'Velocity Improvement', 'verbose_name_plural': 'Velocity Improvements'},
        ),
    ]