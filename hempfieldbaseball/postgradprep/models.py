from django.db import models

from hempfieldbaseball.colleges.models import College


class CollegeCampPageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("college")


class CollegeCamp(models.Model):
    college_camp_id = models.SmallAutoField(primary_key=True)
    college = models.ForeignKey(
        College,
        db_column="college_id",
        verbose_name="College",
        related_name="college_camps",
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    link = models.URLField(max_length=100)

    objects = CollegeCampPageManager()

    class Meta:
        db_table = "CollegeCamp"
        verbose_name = "College Camp"
        verbose_name_plural = "College Camps"

    def __str__(self):
        return f"{self.date} {self.college.name} Camp"
