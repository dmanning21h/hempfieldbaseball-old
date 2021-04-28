from django.shortcuts import render

from . import services as alumni_service


def college_alumni(request):
    alumni_classes = alumni_service.get_alumni_classes()

    context = {
        'alumni_classes': alumni_classes
    }

    return render(request, 'alumni/college.html', context)
