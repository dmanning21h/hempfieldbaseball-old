from django.db import models
from django.db.models import Prefetch


class PlayerPageManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .prefetch_related(
                Prefetch(
                    "roster_infos",
                    TeamPlayer.objects.select_related(
                        "team", "position", "height"
                    ).order_by("-team__year"),
                )
            )
        )


class ActivePlayerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class TeamPageManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .prefetch_related(
                Prefetch(
                    "players",
                    TeamPlayer.objects.select_related(
                        "personal_info", "position", "height"
                    ),
                ),
                Prefetch(
                    "coaches", TeamCoach.objects.select_related("personal_info", "role")
                ),
            )
        )


class Player(models.Model):
    BATS_CHOICES = (("R", "R"), ("L", "L"), ("S", "S"))
    THROWS_CHOICES = (("R", "R"), ("L", "L"))

    player_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    player_link = models.CharField(
        max_length=30, unique=True, blank=True, null=True, default=None
    )
    graduation_year = models.PositiveSmallIntegerField()
    bats = models.CharField(max_length=1, choices=BATS_CHOICES, default="R")
    throws = models.CharField(max_length=1, choices=THROWS_CHOICES, default="R")
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    page_objects = PlayerPageManager()
    active_players = ActivePlayerManager()

    class Meta:
        db_table = "Player"
        ordering = ["-is_active", "last_name"]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Coach(models.Model):
    coach_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    coach_link = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "Coach"
        verbose_name_plural = "Coaches"
        ordering = ["last_name"]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class TeamPlayer(models.Model):
    team_player_id = models.AutoField(primary_key=True)
    personal_info = models.ForeignKey(
        "Player",
        db_column="player_id",
        verbose_name="Player",
        related_name="roster_infos",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        "Team",
        db_column="team_id",
        verbose_name="Team",
        related_name="players",
        on_delete=models.CASCADE,
    )
    height = models.ForeignKey(
        "Height", db_column="height_id", verbose_name="Height", on_delete=models.PROTECT
    )
    weight = models.PositiveSmallIntegerField()
    position = models.ForeignKey(
        "Position",
        db_column="position_id",
        verbose_name="Position",
        on_delete=models.PROTECT,
    )
    number = models.PositiveSmallIntegerField(default=0)
    roster_photo = models.ImageField(upload_to="player-portraits")

    class Meta:
        db_table = "TeamPlayer"
        verbose_name = "Team Player"
        verbose_name_plural = "Team Players"
        ordering = ["number"]

    def __str__(self):
        return f"{self.team.year} {self.personal_info.full_name()}"


class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    abbr = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = "Position"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Height(models.Model):
    height_id = models.AutoField(primary_key=True)
    height = models.PositiveSmallIntegerField(unique=True)

    def height_feet_inches(self):
        feet = int(self.height / 12)
        inches = int(self.height % 12)
        return f"{feet}'{inches}\""

    class Meta:
        db_table = "Height"
        ordering = ["height"]

    def __str__(self):
        return self.height_feet_inches()


class TeamCoach(models.Model):
    team_coach_id = models.AutoField(primary_key=True)
    personal_info = models.ForeignKey(
        "Coach",
        db_column="coach_id",
        verbose_name="Coach",
        related_name="roster_infos",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        "Team",
        db_column="team_id",
        verbose_name="Team",
        related_name="coaches",
        on_delete=models.CASCADE,
    )
    role = models.ForeignKey(
        "CoachRole",
        db_column="coach_role_id",
        verbose_name="Coach Role",
        on_delete=models.PROTECT,
    )
    roster_photo = models.ImageField(upload_to="coach-portraits")

    class Meta:
        db_table = "TeamCoach"
        verbose_name = "Team Coach"
        verbose_name_plural = "Team Coaches"

    def __str__(self):
        return f"{self.team.year} {self.personal_info.full_name()}"


class CoachRole(models.Model):
    coach_role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    priority = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "CoachRole"
        verbose_name = "Coach Role"
        verbose_name_plural = "Coach Roles"
        ordering = ["priority"]

    def __str__(self):
        return self.name


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    year = models.PositiveSmallIntegerField(unique=True)
    team_photo = models.ImageField(upload_to="team-photos", blank=True, null=True)

    objects = models.Manager()
    page_objects = TeamPageManager()

    class Meta:
        db_table = "Team"
        ordering = ["-year"]

    def __str__(self):
        return f"{self.year} Team Roster"
