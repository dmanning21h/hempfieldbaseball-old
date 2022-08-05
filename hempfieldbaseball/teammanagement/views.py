from django.shortcuts import render, get_object_or_404

from hempfieldbaseball.playerprogress.enums import TimeTypes
from .models import Team, Player


def roster(request, year=None):
    if year:
        team = get_object_or_404(Team.page_objects, year=year)
    else:
        team = Team.page_objects.all().first()

    context = {
        "team": team,
    }

    return render(request, "teammanagement/roster.html", context)


def player(request, player_link):
    player = get_object_or_404(Player.page_objects, player_link=player_link)
    roster_info = player.roster_infos.first()

    has_body_weights = player.bodyweight_records.exists()
    has_velocities = player.velocity_records.exists()
    has_pulldowns = player.pulldown_records.exists()
    has_plyo_drill_velocities = player.plyodrillvelocity_records.exists()
    has_times = player.time_records.filter(
        ttype__name=TimeTypes.SIXTY_YARD_DASH
    ).exists()
    has_data = has_body_weights or has_velocities or has_times

    context = {
        "player": player,
        "roster_info": roster_info,
        "has_body_weights": has_body_weights,
        "has_velocities": has_velocities,
        "has_pulldowns": has_pulldowns,
        "has_plyo_drill_velocities": has_plyo_drill_velocities,
        "has_times": has_times,
        "has_data": has_data,
    }

    return render(request, "teammanagement/player.html", context)
