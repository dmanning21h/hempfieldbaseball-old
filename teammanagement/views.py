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
    player = tms.get_player_from_link(player_link)
    roster_info = player.roster_infos.last()
    
    context = {
        'player': player,
        'roster_info': roster_info
    }

    return render(request, 'teammanagement/player.html', context)
