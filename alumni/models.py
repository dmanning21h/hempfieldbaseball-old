from django.db import models

from teammanagement.models import Player


class AlumniPlayer(models.Model):
    alumni_player_id = models.AutoField(primary_key=True)
    info = models.ForeignKey(Player, db_column='player_id',
                             verbose_name='Player',
                             blank=True, null=True,
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    college = models.CharField(max_length=50)
    alumni_class = models.ForeignKey('AlumniClass',
                                     db_column='alumni_class_id',
                                     verbose_name="Alumni Class",
                                     related_name='players',
                                     on_delete=models.CASCADE)
    college_roster_link = models.CharField(max_length=75, unique=True)
    college_roster_photo = models.ImageField(upload_to='alumni-portraits')

    class Meta:
        db_table = "AlumniPlayer"
        verbose_name = "Alumni Player"
        verbose_name_plural = "Alumni Players"
        ordering = ['last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} Alumni"


class AlumniClass(models.Model):
    alumni_class_id = models.AutoField(primary_key=True)
    year = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        db_table = "AlumniClass"
        verbose_name = "Alumni Class"
        verbose_name_plural = "Alumni Classes"
        ordering = ['-year']

    def __str__(self):
        return f"{self.year} Alumni Class"
