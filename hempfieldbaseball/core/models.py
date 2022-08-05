from django.db import models

from hempfieldbaseball.teammanagement.models import Player


class DateModel(models.Model):
    date = models.DateField()

    class Meta:
        abstract = True


class PlayerDateModel(DateModel):
    player = models.ForeignKey(
        Player,
        db_column="player_id",
        verbose_name="Player",
        related_name="%(class)s_records",
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True
