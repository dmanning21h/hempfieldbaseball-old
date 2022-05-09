from django.db import models


class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    primary_color = models.CharField(max_length=7)
    secondary_color = models.CharField(max_length=7)
    logo = models.ImageField(upload_to="college-logos")
    division = models.ForeignKey('Division',
                                db_column='division_id',
                                verbose_name="Division",
                                related_name='colleges',
                                on_delete=models.PROTECT)

    class Meta:
        db_table = "College"
        verbose_name = "College"
        verbose_name_plural = "Colleges"
        ordering = ['name']

    def __str__(self):
        return self.name


class Division(models.Model):
    division_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=15,
                            unique=True)

    class Meta:
        db_table = "Division"
        verbose_name = "Division"
        verbose_name_plural = "Divisions"
        ordering = ['name']

    def __str__(self):
        return self.name
