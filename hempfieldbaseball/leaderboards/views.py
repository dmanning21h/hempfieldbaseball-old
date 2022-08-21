from django.shortcuts import render

from . import services as ls
from hempfieldbaseball.velocities.models import Velocity


def index(request):
    context = {}

    return render(request, "leaderboards/index.html", context)


def pitching_velocity_improvement(request):
    return _render_velocity_improvement_leaderboard(request, Velocity.Position.PITCHING)


def exit_velocity_improvement(request):
    return _render_velocity_improvement_leaderboard(request, Velocity.Position.EXIT)


def _render_velocity_improvement_leaderboard(request, velocity_position):
    top_improvements = ls.get_velocity_improvement_leaders(velocity_position.value)

    context = {
        "velocity_name": velocity_position.label,
        "top_improvements": top_improvements,
    }

    return render(request, "leaderboards/improvement/velocity.html", context)


def misc_improvement(request):
    body_weight_improvement_leaders = ls.get_body_weight_improvement_leaders()

    context = {
        "body_weight_improvement_leaders": body_weight_improvement_leaders,
    }

    return render(request, "leaderboards/improvement/misc.html", context)
