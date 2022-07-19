from django.shortcuts import render

from . import services as tms
from playerprogress import services as pps
from playerprogress.enums import TimeTypes


def roster(request, year=None):
    if year:
        team = tms.get_team_by_year(year)
    else:
        team = tms.get_current_team()

    context = {
        'team': team,
    }

    return render(request, 'teammanagement/roster.html', context)


def player(request, player_link):
    player = tms.get_player_from_link(player_link)
    roster_info = player.roster_infos.first()

    has_body_weights = player.body_weights.exists()
    has_velocities = player.velocities.exists()
    has_pulldowns = player.pulldowns.exists()
    has_times = player.times.filter(ttype__name=TimeTypes.SIXTY_YARD_DASH).exists()
    has_data = has_body_weights or has_velocities or has_times


    context = {
        'player': player,
        'roster_info': roster_info,

        'has_body_weights': has_body_weights,
        'has_velocities': has_velocities,
        'has_pulldowns': has_pulldowns,
        'has_times': has_times,
        'has_data': has_data
    }

    return render(request, 'teammanagement/player.html', context)
