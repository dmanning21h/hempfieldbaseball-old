# Generated by Django 3.2.12 on 2022-08-21 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velocities', '0004_delete_velocityimprovement'),
    ]

    operations = [
        migrations.AddField(
            model_name='velocity',
            name='position',
            field=models.CharField(choices=[('E', 'Exit'), ('P', 'Pitching'), ('OF', 'Outfield'), ('IF', 'Infield'), ('C', 'Catching')], max_length=2, null=True),
        ),
    ]
