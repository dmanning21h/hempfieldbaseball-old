# Generated by Django 3.2.3 on 2021-08-13 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20210531_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='websitelinktype',
            options={'verbose_name': 'Link Type', 'verbose_name_plural': 'Link Types'},
        ),
        migrations.RenameField(
            model_name='websitelinktype',
            old_name='website_link_type_id',
            new_name='link_type_id',
        ),
        migrations.RemoveField(
            model_name='websitelinktype',
            name='is_video',
        ),
        migrations.AlterModelTable(
            name='websitelinktype',
            table='LinkType',
        ),
    ]
