# Generated by Django 3.2.12 on 2022-09-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("colleges", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="college",
            name="division_choice",
            field=models.CharField(
                choices=[
                    ("NC1", "NCAA Division I"),
                    ("NC2", "NCAA Division II"),
                    ("NC3", "NCAA Division III"),
                    ("NAI", "NAIA"),
                    ("JC1", "NJCAA Division I"),
                    ("JC2", "NJCAA Division II"),
                    ("JC3", "NJCAA Division III"),
                ],
                max_length=3,
                null=True,
            ),
        ),
    ]
