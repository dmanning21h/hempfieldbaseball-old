from django.db import models
from django.db.models import Prefetch

from postgradprep.models import College
from teammanagement.enums import TeamManagementModels


class AlumniClassManager(models.Manager):
    def get_queryset(self):
        return (super().get_queryset()
                .prefetch_related(
                    Prefetch('players',
                             AlumniPlayer.objects.select_related(
                                 'info',
                                 'college'))))


class AlumniPlayer(models.Model):
    alumni_player_id = models.AutoField(primary_key=True)
    info = models.ForeignKey(TeamManagementModels.PLAYER, db_column='player_id',
                             verbose_name='Player',
                             on_delete=models.CASCADE)
    alumni_class = models.ForeignKey('AlumniClass',
                                     db_column='alumni_class_id',
                                     verbose_name="Alumni Class",
                                     related_name='players',
                                     on_delete=models.PROTECT)
    college = models.ForeignKey(College, db_column='college_id',
                                verbose_name="College",
                                related_name='alumni_players',
                                on_delete=models.PROTECT)
    college_roster_link = models.URLField(max_length=75, unique=True)
    college_roster_photo = models.ImageField(upload_to='alumni-portraits',
                                            blank=True, null=True)

    class Meta:
        db_table = "AlumniPlayer"
        verbose_name = "Alumni Player"
        verbose_name_plural = "Alumni Players"
        ordering = ['info__last_name']

    def __str__(self):
        return f"{self.info.first_name} {self.info.last_name} Alumni"


class AlumniClass(models.Model):
    alumni_class_id = models.AutoField(primary_key=True)
    year = models.PositiveSmallIntegerField(unique=True)

    objects = AlumniClassManager()

    class Meta:
        db_table = "AlumniClass"
        verbose_name = "Alumni Class"
        verbose_name_plural = "Alumni Classes"
        ordering = ['-year']

    def __str__(self):
        return f"{self.year} Alumni Class"
