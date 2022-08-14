from datetime import datetime

from django.shortcuts import render

from .models import CollegeCamp


def college_camps(request):
    college_camps = CollegeCamp.objects.filter(date__gt=datetime.today()).order_by(
        "date"
    )

    context = {"college_camps": college_camps}

    return render(request, "postgradprep/college-camps.html", context)
