from django.shortcuts import render

from . import services as ls
from hempfieldbaseball.velocities.enums import VelocityTypes


def index(request):
    context = {}

    return render(request, "leaderboards/index.html", context)


def velocity_performance(request):
    velocity_leader_data = ls.get_velocity_leaders()

    context = {
        "velocity_leader_data": velocity_leader_data,
    }

    return render(request, "leaderboards/performance/velocity.html", context)


def time_performance(request):
    time_leader_data = ls.get_time_leaders()

    context = {
        "time_leader_data": time_leader_data,
    }

    return render(request, "leaderboards/performance/time.html", context)


def pitching_velocity_improvement(request):
    return _render_velocity_improvement_leaderboard(
        request, VelocityTypes.PITCHING.value
    )


def exit_velocity_improvement(request):
    return _render_velocity_improvement_leaderboard(request, VelocityTypes.EXIT.value)


def _render_velocity_improvement_leaderboard(request, velocity_name):
    top_improvements = ls.get_velocity_improvement_leaders(velocity_name)

    context = {
        "velocity_name": velocity_name,
        "top_improvements": top_improvements,
    }

    return render(request, "leaderboards/improvement/velocity.html", context)


def time_improvement(request):
    time_improvement_leader_data = ls.get_time_improvement_leaders()

    context = {"time_improvement_leader_data": time_improvement_leader_data}

    return render(request, "leaderboards/improvement/time.html", context)


def misc_improvement(request):
    body_weight_improvement_leaders = ls.get_body_weight_improvement_leaders()

    context = {
        "body_weight_improvement_leaders": body_weight_improvement_leaders,
    }

    return render(request, "leaderboards/improvement/misc.html", context)
