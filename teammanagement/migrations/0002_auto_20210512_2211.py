# Generated by Django 3.1.6 on 2021-05-13 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coachrole',
            options={'ordering': ['priority'], 'verbose_name': 'Coach Role', 'verbose_name_plural': 'Coach Roles'},
        ),
        migrations.AddField(
            model_name='coachrole',
            name='priority',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
