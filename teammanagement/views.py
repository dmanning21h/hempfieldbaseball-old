from django.shortcuts import render

from . import services as tms
from playerprogress import services as pps


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
    player_id = tms.get_player_id_from_link(player_link)

    player = tms.get_latest_team_player_by_player_id(player_id)

    context = {
        'player': player

    }

    return render(request, 'teammanagement/player.html', context)
