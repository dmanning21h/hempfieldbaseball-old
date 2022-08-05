from .models import AlumniClass


def get_alumni_classes():
    return AlumniClass.objects.all()
