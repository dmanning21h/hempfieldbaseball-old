# Generated by Django 3.2.12 on 2022-08-14 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Division",
                    fields=[
                        (
                            "division_id",
                            models.SmallAutoField(primary_key=True, serialize=False),
                        ),
                        ("name", models.CharField(max_length=15, unique=True)),
                    ],
                    options={
                        "verbose_name": "Division",
                        "verbose_name_plural": "Divisions",
                        "db_table": "Division",
                        "ordering": ["name"],
                    },
                ),
                migrations.CreateModel(
                    name="College",
                    fields=[
                        (
                            "college_id",
                            models.AutoField(primary_key=True, serialize=False),
                        ),
                        ("name", models.CharField(max_length=50, unique=True)),
                        ("primary_color", models.CharField(max_length=7)),
                        ("secondary_color", models.CharField(max_length=7)),
                        ("logo", models.ImageField(upload_to="college-logos")),
                        (
                            "division",
                            models.ForeignKey(
                                db_column="division_id",
                                on_delete=django.db.models.deletion.PROTECT,
                                related_name="colleges",
                                to="colleges.division",
                                verbose_name="Division",
                            ),
                        ),
                    ],
                    options={
                        "verbose_name": "College",
                        "verbose_name_plural": "Colleges",
                        "db_table": "College",
                        "ordering": ["name"],
                    },
                ),
            ],
            database_operations=[],
        ),
    ]
