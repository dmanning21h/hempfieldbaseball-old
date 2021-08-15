import math
from datetime import timedelta

from django.db import models

from teammanagement.models import Player


class LiftType(models.Model):
    lift_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "LiftType"
        verbose_name = "Lift Type"
        verbose_name_plural = "Lift Types"
        ordering = ['order']

    def __str__(self):
        return self.name


class Lift(models.Model):
    lift_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='lifts',
                               on_delete=models.CASCADE)
    date = models.DateField()
    ttype = models.ForeignKey('LiftType', db_column='lift_type_id',
                              verbose_name="Lift Type",
                              related_name='lifts',
                              on_delete=models.CASCADE)
    set1 = models.ForeignKey('LiftSet', db_column='set1_id',
                             verbose_name="Set 1",
                             related_name='set1_lifts',
                             on_delete=models.PROTECT)
    set2 = models.ForeignKey('LiftSet', db_column='set2_id',
                             verbose_name="Set 2",
                             related_name='set2_lifts',
                             on_delete=models.PROTECT)
    set3 = models.ForeignKey('LiftSet', db_column='set3_id',
                             verbose_name="Set 3",
                             related_name='set3_lifts',
                             on_delete=models.PROTECT)

    def strength_points(self):
        set_points = []
        for lift_set_id in [self.set1, self.set2, self.set3]:
            set_points.append(
                StrengthIncrement.objects
                .filter(lift_type=self.ttype)
                .get(lift_set=lift_set_id)
                .strength_points
            )
        return sum(set_points)

    def sets(self):
        return f"{self.set1} {self.set2} {self.set3}"

    class Meta:
        db_table = "Lift"
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} {self.player} {self.ttype} ({self.sets()})"


class LiftSet(models.Model):
    lift_set_id = models.AutoField(primary_key=True)
    weight = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "LiftSet"
        verbose_name = "Lift Set"
        verbose_name_plural = "Lift Sets"

    def __str__(self):
        return f"{self.weight}x{self.reps}"


class StrengthIncrement(models.Model):
    increment_id = models.AutoField(primary_key=True)
    lift_type = models.ForeignKey('LiftType', db_column='lift_type_id',
                                  verbose_name="Lift Type",
                                  related_name='strength_increments',
                                  on_delete=models.CASCADE)
    lift_set = models.ForeignKey('LiftSet', db_column='lift_set_id',
                                 verbose_name="Set Weight x Reps",
                                 related_name='strength_increments',
                                 on_delete=models.PROTECT)
    strength_points = models.FloatField(verbose_name="Strength Points")

    class Meta:
        db_table = "StrengthIncrement"
        verbose_name = "Lift Strength Increment"
        verbose_name_plural = "Lift Strength Increments"

    def __str__(self):
        return f"{self.lift_type} ({self.lift_set}): {self.strength_points} SP"


class LiftImprovement(models.Model):
    lift_improvement_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='lift_improvements',
                               on_delete=models.CASCADE)
    ttype = models.ForeignKey('LiftType', db_column='lift_type_id',
                              verbose_name="Lift Type",
                              related_name='improvements',
                              on_delete=models.CASCADE)
    baseline = models.ForeignKey('Lift', db_column='baseline_lift_id',
                                 verbose_name="Baseline",
                                 related_name='baseline_lift_improvements',
                                 null=True,
                                 on_delete=models.PROTECT)
    latest = models.ForeignKey('Lift', db_column='latest_lift_id',
                               verbose_name="Latest",
                               related_name='latest_lift_improvements',
                               null=True,
                               on_delete=models.PROTECT)
    improvement = models.FloatField(default=0)

    class Meta:
        db_table = "LiftImprovement"
        verbose_name = "Lift Improvement"
        verbose_name_plural = "Lift Improvements"
        ordering = ['-player__is_active', 'player__last_name', 'ttype__order']

    def __str__(self):
        return f"{self.player} {self.ttype} Improvement"


class VelocityType(models.Model):
    velocity_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "VelocityType"
        verbose_name = "Velocity Type"
        verbose_name_plural = "Velocity Types"
        ordering = ['order']

    def __str__(self):
        return self.name


class Velocity(models.Model):
    velocity_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='velocities',
                               on_delete=models.CASCADE)
    date = models.DateField()
    ttype = models.ForeignKey('VelocityType',
                              db_column='velocity_type_id',
                              verbose_name="Velocity Type",
                              related_name='velocities',
                              on_delete=models.CASCADE)
    velocity = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "Velocity"
        verbose_name_plural = "Velocities"
        ordering = ['-date']

    def __str__(self):
        return f"{self.player} {self.date} {self.ttype} Velocity"


class VelocityImprovement(models.Model):
    velocity_improvement_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='velocity_improvements',
                               on_delete=models.CASCADE)
    ttype = models.ForeignKey('VelocityType',
                              db_column='velocity_type_id',
                              verbose_name="Velocity Type",
                              related_name='improvements',
                              on_delete=models.CASCADE)
    baseline = models.ForeignKey('Velocity', db_column='baseline_velocity_id',
                                 verbose_name="Baseline",
                                 related_name='baseline_velocity_improvements',
                                 null=True,
                                 on_delete=models.PROTECT)
    latest = models.ForeignKey('Velocity', db_column='latest_velocity_id',
                               verbose_name="Latest",
                               related_name='latest_velocity_improvements',
                               null=True,
                               on_delete=models.PROTECT)
    improvement = models.SmallIntegerField(default=0)

    class Meta:
        db_table = "VelocityImprovement"
        verbose_name = "Velocity Improvement"
        verbose_name_plural = "Velocity Improvements"
        ordering = ['-player__is_active', 'player__last_name', 'ttype__order']

    def __str__(self):
        return f"{self.player} {self.ttype} Improvement"


class TimeType(models.Model):
    time_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_speed = models.BooleanField(default=True)

    class Meta:
        db_table = "TimeType"
        verbose_name = "Time Type"
        verbose_name_plural = "Time Types"
        ordering = ['order']

    def __str__(self):
        return self.name


class Time(models.Model):
    time_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='times',
                               on_delete=models.CASCADE)
    date = models.DateField()
    ttype = models.ForeignKey('TimeType',
                              db_column='time_type_id',
                              verbose_name="Time Type",
                              related_name='times',
                              on_delete=models.CASCADE)
    time = models.DurationField()

    def formatted_time(self):
        time = self.time

        if time < timedelta(seconds=45):
            seconds = time.seconds
            hundredths = f"{time.microseconds:06}"[:2]
            formatted_time = f"{seconds}.{hundredths} s"
        else:
            minutes = math.floor(time.seconds / 60)
            seconds = f"{time.seconds % 60:02}"
            formatted_time = f"{minutes}:{seconds}"

        return formatted_time

    class Meta:
        db_table = "Time"
        ordering = ['-date']

    def __str__(self):
        return f"{self.player} {self.date} {self.ttype} Time"


class TimeImprovement(models.Model):
    time_improvement_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='time_improvements',
                               on_delete=models.CASCADE)
    ttype = models.ForeignKey('TimeType',
                              db_column='time_type_id',
                              verbose_name="Time Type",
                              related_name='improvements',
                              on_delete=models.CASCADE)
    baseline = models.ForeignKey('Time', db_column='baseline_time_id',
                                 verbose_name="Baseline",
                                 related_name='baseline_time_improvements',
                                 null=True,
                                 on_delete=models.PROTECT)
    latest = models.ForeignKey('Time', db_column='latest_time_id',
                               verbose_name="Latest",
                               related_name='latest_time_improvements',
                               null=True,
                               on_delete=models.PROTECT)
    improvement = models.DurationField(default=timedelta(0))
    is_seconds = models.BooleanField(default=True)

    def formatted_improvement(self):
        improvement = self.improvement

        if self.is_seconds:
            seconds = improvement.seconds
            hundredths = f"{improvement.microseconds:06}"[:2]
            formatted_improvement = f"{seconds}.{hundredths} s"
        else:
            minutes = math.floor(improvement.seconds / 60)
            seconds = f"{improvement.seconds % 60:02}"
            formatted_improvement = f"{minutes}:{seconds}"

        return formatted_improvement

    class Meta:
        db_table = "TimeImprovement"
        verbose_name = "Time Improvement"
        verbose_name_plural = "Time Improvements"
        ordering = ['-player__is_active', 'player__last_name', 'ttype__order']

    def __str__(self):
        return f"{self.player} {self.ttype} Improvement"


class DistanceType(models.Model):
    distance_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "DistanceType"
        verbose_name = "Distance Type"
        verbose_name_plural = "Distance Types"
        ordering = ['order']

    def __str__(self):
        return self.name


class Distance(models.Model):
    distance_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='distances',
                               on_delete=models.CASCADE)
    date = models.DateField()
    ttype = models.ForeignKey('DistanceType',
                              db_column='distance_type_id',
                              verbose_name="Distance Type",
                              related_name='distances',
                              on_delete=models.CASCADE)
    distance = models.FloatField()

    class Meta:
        db_table = "Distance"
        ordering = ['-date']

    def __str__(self):
        return f"{self.player} {self.date} {self.ttype} Distance"


class DistanceImprovement(models.Model):
    distance_improvement_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='distance_improvements',
                               on_delete=models.CASCADE)
    ttype = models.ForeignKey('DistanceType',
                              db_column='distance_type_id',
                              verbose_name="Distance Type",
                              related_name='improvements',
                              on_delete=models.CASCADE)
    baseline = models.ForeignKey('Distance', db_column='baseline_distance_id',
                                 verbose_name="Baseline",
                                 related_name='baseline_distance_improvements',
                                 null=True,
                                 on_delete=models.PROTECT)
    latest = models.ForeignKey('Distance', db_column='latest_distance_id',
                               verbose_name="Latest",
                               related_name='latest_distance_improvements',
                               null=True,
                               on_delete=models.PROTECT)
    improvement = models.FloatField(default=0)

    class Meta:
        db_table = "DistanceImprovement"
        verbose_name = "Distance Improvement"
        verbose_name_plural = "Distance Improvements"
        ordering = ['-player__is_active', 'player__last_name', 'ttype__order']

    def __str__(self):
        return f"{self.player} {self.ttype} Improvement"


class BodyWeight(models.Model):
    body_weight_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='body_weights',
                               on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField(verbose_name="Body Weight")

    class Meta:
        db_table = "BodyWeight"
        verbose_name = "Body Weight"
        verbose_name_plural = "Body Weights"
        ordering = ['-date']

    def __str__(self):
        return f"{self.player} {self.date} Body Weight"


class BodyWeightImprovement(models.Model):
    body_weight_improvement_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, db_column='player_id',
                               verbose_name="Player",
                               related_name='body_weight_improvements',
                               on_delete=models.CASCADE)
    baseline = models.ForeignKey('BodyWeight',
                                 db_column='baseline_body_weight_id',
                                 verbose_name="Baseline",
                                 related_name='baseline_body_weight_improvements',
                                 null=True,
                                 on_delete=models.PROTECT)
    latest = models.ForeignKey('BodyWeight',
                               db_column='latest_body_weight_id',
                               verbose_name="Latest",
                               related_name='latest_body_weight_improvements',
                               null=True,
                               on_delete=models.PROTECT)
    improvement = models.FloatField(default=0)

    class Meta:
        db_table = "BodyWeightImprovement"

    def __str__(self):
        return f"{self.player} Body Weight Improvement"
