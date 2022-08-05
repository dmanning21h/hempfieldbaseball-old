from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from hempfieldbaseball.teammanagement.models import Player
from .enums import VelocityTypes
from .models import Pulldown, PlyoDrillVelocity


def get_player_velocities_with_dates(request):
    """
    Returns all velocities (date, velocity) of each type for a given player.
    Also returns a list of all dates for velocities for use with Chart.js.
    """
    player_id = request.GET.get("player_id")
    player = get_object_or_404(Player, pk=player_id)
    all_velocities = player.velocity_records(manager="velocities_with_types").all()

    (
        exit_velocities,
        pitching_velocities,
        outfield_velocities,
        infield_velocities,
        catcher_velocities,
        all_dates,
    ) = ([] for _ in range(6))
    list_map = {
        VelocityTypes.EXIT: exit_velocities,
        VelocityTypes.PITCHING: pitching_velocities,
        VelocityTypes.OUTFIELD: outfield_velocities,
        VelocityTypes.INFIELD: infield_velocities,
        VelocityTypes.CATCHER: catcher_velocities,
    }

    for velocity in all_velocities:
        ttype = velocity.ttype.name
        date = velocity.date.strftime("%m/%d/%y")
        velo = velocity.velocity

        list_map[ttype].append((date, velo))
        all_dates.append(date)

    response = {
        "exit": exit_velocities,
        "pitching": pitching_velocities,
        "outfield": outfield_velocities,
        "infield": infield_velocities,
        "allDates": all_dates,
    }

    return JsonResponse(response)


def get_player_pulldowns_with_dates(request):
    """
    Returns all pulldowns (date, velocity) of each type for a given player.
    Also returns a list of all dates for velocities for use with Chart.js.
    """
    player_id = request.GET.get("player_id")
    player = get_object_or_404(Player, pk=player_id)

    three_ounce, four_ounce, five_ounce, six_ounce, seven_ounce, all_dates = (
        [] for _ in range(6)
    )
    list_map = {
        Pulldown.BallWeights.THREE_OUNCE: three_ounce,
        Pulldown.BallWeights.FOUR_OUNCE: four_ounce,
        Pulldown.BallWeights.FIVE_OUNCE: five_ounce,
        Pulldown.BallWeights.SIX_OUNCE: six_ounce,
        Pulldown.BallWeights.SEVEN_OUNCE: seven_ounce,
    }

    for pulldown in player.pulldown_records.all():
        weight = pulldown.ball_weight
        date = pulldown.date.strftime("%m/%d/%y")
        velo = pulldown.velocity

        list_map[weight].append((date, velo))
        all_dates.append(date)

    response = {
        "three": three_ounce,
        "four": four_ounce,
        "five": five_ounce,
        "six": six_ounce,
        "seven": seven_ounce,
        "allDates": all_dates,
    }

    return JsonResponse(response)


def get_player_plyo_drill_velocities_with_dates(request):
    """
    Returns all plyo drill velocities (date, velocity) of each type for a given player.
    Also returns a list of all dates for velocities for use with Chart.js.
    """
    player_id = request.GET.get("player_id")
    player = get_object_or_404(Player, pk=player_id)

    drill_map = {
        PlyoDrillVelocity.Drill.FUNNEL_FRONT: _new_plyo_drill_velocity_object(),
        PlyoDrillVelocity.Drill.STEP_BACK: _new_plyo_drill_velocity_object(),
        PlyoDrillVelocity.Drill.DROP_STEP: _new_plyo_drill_velocity_object(),
        PlyoDrillVelocity.Drill.WALKING_WINDUP: _new_plyo_drill_velocity_object(),
    }

    for plyo_drill_velocity in player.plyodrillvelocity_records.all():
        drill = plyo_drill_velocity.drill
        weight = plyo_drill_velocity.ball_weight
        date = plyo_drill_velocity.date.strftime("%m/%d/%y")
        velo = plyo_drill_velocity.velocity

        drill_map[drill][weight].append((date, velo))
        drill_map[drill]["all_dates"].append(date)

    response = {
        "funnel_front": drill_map[PlyoDrillVelocity.Drill.FUNNEL_FRONT],
        "step_back": drill_map[PlyoDrillVelocity.Drill.STEP_BACK],
        "drop_step": drill_map[PlyoDrillVelocity.Drill.DROP_STEP],
        "walking_windup": drill_map[PlyoDrillVelocity.Drill.WALKING_WINDUP],
    }

    return JsonResponse(response)


def _new_plyo_drill_velocity_object():
    return {
        PlyoDrillVelocity.BallWeight.BLUE: [],
        PlyoDrillVelocity.BallWeight.RED: [],
        PlyoDrillVelocity.BallWeight.YELLOW: [],
        PlyoDrillVelocity.BallWeight.GRAY: [],
        "all_dates": [],
    }