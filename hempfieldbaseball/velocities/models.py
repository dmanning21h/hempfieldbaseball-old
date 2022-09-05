from django.db import models

from hempfieldbaseball.core.models import PlayerDateModel


class BaseVelocityModel(PlayerDateModel):
    velocity = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True


class Velocity(BaseVelocityModel):
    class Position(models.TextChoices):
        EXIT = "E", "Exit"
        PITCHING = "P", "Pitching"
        OUTFIELD = "OF", "Outfield"
        INFIELD = "IF", "Infield"
        CATCHING = "C", "Catching"

    velocity_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=2, choices=Position.choices)

    objects = models.Manager()

    class Meta:
        db_table = "Velocity"
        verbose_name_plural = "Velocities"
        ordering = ["date"]

    def __str__(self):
        return f"{self.player} {self.date} {self.get_position_display()} Velocity"


class WeightedBallVelocity(BaseVelocityModel):
    class Drill(models.TextChoices):
        MOUND = "M", ("Mound")
        PULLDOWN = "P", ("Pulldown")

    class BallWeight(models.TextChoices):
        THREE_OUNCE = "3", "3oz"
        FOUR_OUNCE = "4", "4oz"
        FIVE_OUNCE = "5", "5oz"
        SIX_OUNCE = "6", "6oz"
        SEVEN_OUNCE = "7", "7oz"

    pulldown_id = models.AutoField(primary_key=True)
    drill = models.CharField(max_length=1, choices=Drill.choices, default="P")
    ball_weight = models.CharField(max_length=1, choices=BallWeight.choices)

    objects = models.Manager()

    class Meta:
        db_table = "WeightedBallVelocity"
        verbose_name = "Weighted Ball Velocity"
        verbose_name_plural = "Weighted Ball Velocities"
        ordering = ["date"]

    def __str__(self):
        return f"{self.player} {self.date} {self.get_ball_weight_display()} Pulldown"


class PlyoDrillVelocity(BaseVelocityModel):
    class Drill(models.TextChoices):
        FUNNEL_FRONT = "FF", ("Funnel Front")
        STEP_BACK = "SB", ("Step Back")
        DROP_STEP = "DS", ("Drop Step")
        WALKING_WINDUP = "WW", ("Walking Windup")

    class BallWeight(models.TextChoices):
        BLUE = "450", "450g"
        RED = "225", "225g"
        YELLOW = "150", "150g"
        GRAY = "100", "100g"

    plyo_drill_velocity_id = models.AutoField(primary_key=True)
    drill = models.CharField(max_length=2, choices=Drill.choices)
    ball_weight = models.CharField(max_length=3, choices=BallWeight.choices)

    objects = models.Manager()

    class Meta:
        db_table = "PlyoDrillVelocity"
        verbose_name = "Plyo Drill Velocity"
        verbose_name_plural = "Plyo Drill Velocities"
        ordering = ["date"]

    def __str__(self):
        return (
            f"{self.player} {self.date} {self.get_ball_weight_display()} "
            f"{self.get_drill_display()}"
        )
