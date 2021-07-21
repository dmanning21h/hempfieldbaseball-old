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
    lifts = pps.get_all_player_lifts(player_id)
    velocities = pps.get_all_player_velocities(player_id)
    times = pps.get_all_player_times(player_id)
    distances = pps.get_all_player_distances(player_id)
    body_weights = pps.get_all_player_body_weights(player_id)

    has_data = []
    for metric in [lifts, velocities, times, distances]:
        has_data.extend([True for name, data in metric.items() if data])
    has_data.extend([True for weight in body_weights if weight])

    context = {
        'player':
            player,

        'has_data':
            has_data,

        'lift_data':
            lifts,

        'velocity_data':
            velocities,

        'time_data':
            times,

        'distance_data':
            distances,

        'body_weights':
            body_weights,

    }

    return render(request, 'teammanagement/player.html', context)
