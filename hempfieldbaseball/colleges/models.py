from django.db import models


class College(models.Model):
    class Division(models.TextChoices):
        NCAA1 = "NC1", "NCAA Division I"
        NCAA2 = "NC2", "NCAA Division II"
        NCAA3 = "NC3", "NCAA Division III"
        NAIA = "NAI", "NAIA"
        NJCAA1 = "JC1", "NJCAA Division I"
        NJCAA2 = "JC2", "NJCAA Division II"
        NJCAA3 = "JC3", "NJCAA Division III"

    college_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    primary_color = models.CharField(max_length=7)
    secondary_color = models.CharField(max_length=7)
    logo = models.ImageField(upload_to="college-logos")
    division = models.CharField(max_length=3, choices=Division.choices)

    class Meta:
        db_table = "College"
        verbose_name = "College"
        verbose_name_plural = "Colleges"
        ordering = ["name"]

    def __str__(self):
        return self.name
