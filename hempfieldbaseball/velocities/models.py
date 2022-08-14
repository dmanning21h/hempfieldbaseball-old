from django.db import models

from hempfieldbaseball.core.models import PlayerDateModel


class VelocityWithTypeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("ttype")


class BaseVelocityModel(PlayerDateModel):
    velocity = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True


class VelocityType(models.Model):
    velocity_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    order = models.PositiveSmallIntegerField(default=0)

    objects = models.Manager()

    class Meta:
        db_table = "VelocityType"
        verbose_name = "Velocity Type"
        verbose_name_plural = "Velocity Types"
        ordering = ["order"]

    def __str__(self):
        return self.name


class Velocity(BaseVelocityModel):
    velocity_id = models.AutoField(primary_key=True)
    ttype = models.ForeignKey(
        "VelocityType",
        db_column="velocity_type_id",
        verbose_name="Velocity Type",
        related_name="velocities",
        on_delete=models.CASCADE,
    )

    objects = models.Manager()
    velocities_with_types = VelocityWithTypeManager()

    class Meta:
        db_table = "Velocity"
        verbose_name_plural = "Velocities"
        ordering = ["date"]

    def __str__(self):
        return f"{self.player} {self.date} {self.ttype} Velocity"


class Pulldown(BaseVelocityModel):
    class BallWeights(models.TextChoices):
        THREE_OUNCE = "3", "3oz"
        FOUR_OUNCE = "4", "4oz"
        FIVE_OUNCE = "5", "5oz"
        SIX_OUNCE = "6", "6oz"
        SEVEN_OUNCE = "7", "7oz"

    pulldown_id = models.AutoField(primary_key=True)
    ball_weight = models.CharField(max_length=1, choices=BallWeights.choices)

    objects = models.Manager()

    class Meta:
        db_table = "Pulldown"
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
