from django.db import models


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    abbr = models.CharField(max_length=2, unique=True)

    class Meta:
        db_table = "State"
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ['name']


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "City"
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ['name']


class ZipCode(models.Model):
    zip_code_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5, unique=True)

    class Meta:
        db_table = "ZipCode"
        verbose_name = "Zip Code"
        verbose_name_plural = "Zip Codes"
