from datetime import datetime

from django.db import models


class Player(models.Model):
    BATS_CHOICES = (
            ('R', 'R'),
            ('L', 'L'),
            ('S', 'S')
        )
    THROWS_CHOICES = (
            ('R', 'R'),
            ('L', 'L')
        )

    player_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    player_link = models.CharField(max_length=30, unique=True)
    graduation_year = models.PositiveSmallIntegerField()
    bats = models.CharField(max_length=1, choices=BATS_CHOICES,
                            default='R')
    throws = models.CharField(max_length=1, choices=THROWS_CHOICES,
                              default='R')

    class Meta:
        db_table = "Player"
        ordering = ['last_name']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_graduated(self):
        current_year = datetime.now().year
        current_month = datetime.now().month

        if self.graduation_year < current_year:
            return True
        elif self.graduation_year == current_year and current_month > 6:
            return True
        else:
            return False

    def class_standing(self):
        if self.has_graduated():
            return "Graduated"

        current_year = datetime.now().year
        current_month = datetime.now().month
        year_diff = self.graduation_year - current_year

        if current_month > 6:
            year_diff -= 1

        class_standings = ["Senior", "Junior", "Sophomore", "Freshman", "8th"]

        return class_standings[year_diff]

    def class_standing_abbr(self):
        if self.has_graduated():
            return "GR."

        current_year = datetime.now().year
        current_month = datetime.now().month
        year_diff = self.graduation_year - current_year

        if current_month > 6:
            year_diff -= 1

        class_standings = ["SR.", "JR.", "SO.", "FR.", "8th"]

        return class_standings[year_diff]

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
        ordering = ['last_name']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class TeamPlayer(models.Model):
    team_player_id = models.AutoField(primary_key=True)
    info = models.ForeignKey('Player', db_column='player_id',
                             verbose_name="Player",
                             on_delete=models.CASCADE)
    team = models.ForeignKey('Team', db_column='team_id',
                             verbose_name="Team",
                             related_name='players',
                             on_delete=models.CASCADE)
    height = models.ForeignKey('Height', db_column='height_id',
                               verbose_name='Height',
                               on_delete=models.PROTECT)
    weight = models.PositiveSmallIntegerField()
    position = models.ForeignKey('Position', db_column='position_id',
                                 verbose_name='Position',
                                 on_delete=models.PROTECT)
    number = models.PositiveSmallIntegerField(default=0)
    roster_photo = models.ImageField(upload_to='player-portraits')

    class Meta:
        db_table = "TeamPlayer"
        verbose_name = "Team Player"
        verbose_name_plural = "Team Players"
        ordering = ['number']

    def __str__(self):
        return f"{self.team.year} {self.info.full_name()}"


class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    abbr = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = "Position"
        ordering = ['name']

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
        ordering = ['height']

    def __str__(self):
        return self.height_feet_inches()


class TeamCoach(models.Model):
    team_coach_id = models.AutoField(primary_key=True)
    info = models.ForeignKey('Coach', db_column='coach_id',
                             verbose_name="Coach",
                             on_delete=models.CASCADE)
    team = models.ForeignKey('Team', db_column='team_id',
                             verbose_name="Team",
                             related_name='coaches',
                             on_delete=models.CASCADE)
    role = models.ForeignKey('CoachRole', db_column='coach_role_id',
                             verbose_name='Coach Role',
                             on_delete=models.PROTECT)
    roster_photo = models.ImageField(upload_to='coach-portraits')

    class Meta:
        db_table = "TeamCoach"
        verbose_name = "Team Coach"
        verbose_name_plural = "Team Coaches"

    def __str__(self):
        return f"{self.team.year} {self.info.full_name()}"


class CoachRole(models.Model):
    coach_role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "CoachRole"
        verbose_name = "Coach Role"
        verbose_name_plural = "Coach Roles"
        ordering = ['name']

    def __str__(self):
        return self.name


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    year = models.PositiveSmallIntegerField(unique=True)
    team_photo = models.ImageField(upload_to='team-photos', blank=True,
                                   null=True)

    class Meta:
        db_table = "Team"
        ordering = ['-year']

    def __str__(self):
        return f"{self.year} Team Roster"
