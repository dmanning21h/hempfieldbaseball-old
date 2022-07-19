from xml.dom import pulldom
from django.http import JsonResponse
from django.shortcuts import render

from . import services as pps
from .enums import BallWeights, VelocityTypes
from teammanagement import services as tms


def leaderboards(request):
    context = {}

    return render(request, 'playerprogress/leaderboards.html',
                  context)


def velocity_performance_leaderboards(request):
    velocity_leader_data = pps.get_velocity_leaders()

    context = {
        'velocity_leader_data': velocity_leader_data,
    }

    return render(request, 'playerprogress/performance/velocity.html',
                  context)


def time_performance_leaderboards(request):
    time_leader_data = pps.get_time_leaders()

    context = {
        'time_leader_data': time_leader_data,
    }

    return render(request, 'playerprogress/performance/time.html',
                  context)


def pitching_velocity_improvement_leaderboards(request):
    return _render_velocity_improvement_leaderboard(request, VelocityTypes.PITCHING.value)


def exit_velocity_improvement_leaderboards(request):
    return _render_velocity_improvement_leaderboard(request, VelocityTypes.EXIT.value)


def _render_velocity_improvement_leaderboard(request, velocity_name):
    top_improvements = pps.get_velocity_improvement_leaders(velocity_name)

    context = {
        'velocity_name': velocity_name,
        'top_improvements': top_improvements,
    }

    return render(request, 'playerprogress/improvement/velocity.html',
                  context)


def time_improvement_leaderboards(request):
    time_improvement_leader_data = pps.get_time_improvement_leaders()

    context = {
        'time_improvement_leader_data': time_improvement_leader_data
    }

    return render(request, 'playerprogress/improvement/time.html',
                  context)


def misc_improvement_leaderboards(request):
    body_weight_improvement_leaders = pps.get_body_weight_improvement_leaders()

    context = {
        'body_weight_improvement_leaders':
            body_weight_improvement_leaders,
    }

    return render(request, 'playerprogress/improvement/misc.html', context)


def get_player_body_weights_with_dates(request):
    """
    Returns all body weights (date, body weight) for a given player.
    """
    player_id = request.GET.get('player_id')
    player = tms.get_player_by_id(player_id)

    body_weights, all_dates = ([] for _ in range(2))
    for body_weight in player.body_weights.all():
        date = body_weight.date.strftime('%m/%d/%y')
        body_weights.append((date, body_weight.weight))
        all_dates.append(date)

    response = {
        "bodyWeight": body_weights,
        "allDates": all_dates
    }

    return JsonResponse(response)


def get_player_lifts_with_dates(request):
    """
    Returns all lifts (date, sets, strength points) of each type for a given player.
    Also returns a list of all dates for lifts for use with Chart.js.
    """
    player_id = request.GET.get('player_id')

    deadlift_records = pps.get_player_deadlift_lifts(player_id)
    deadlift_dates = [lift.date.strftime('%m/%d/%y') for lift in deadlift_records]
    deadlift_return_data = [[lift.date.strftime('%m/%d/%y'), lift.strength_points(), lift.sets()] for lift in deadlift_records]

    squat_records = pps.get_player_squat_lifts(player_id)
    squat_dates = [lift.date.strftime('%m/%d/%y') for lift in squat_records]
    squat_return_data = [[lift.date.strftime('%m/%d/%y'), lift.strength_points(), lift.sets()] for lift in squat_records]

    bench_records = pps.get_player_bench_lifts(player_id)
    bench_dates = [lift.date.strftime('%m/%d/%y') for lift in bench_records]
    bench_return_data = [[lift.date.strftime('%m/%d/%y'), lift.strength_points(), lift.sets()] for lift in bench_records]

    all_dates = sorted(deadlift_dates + squat_dates + bench_dates) 

    response = {
        "deadlift": deadlift_return_data,
        "squat": squat_return_data,
        "benchPress": bench_return_data,
        "allDates": all_dates
    }

    return JsonResponse(response)


def get_player_velocities_with_dates(request):
    """
    Returns all velocities (date, velocity) of each type for a given player.
    Also returns a list of all dates for velocities for use with Chart.js.
    """
    player_id = request.GET.get('player_id')
    player = tms.get_player_by_id(player_id)
    all_velocities = player.velocities(manager='velocities_with_types').all()

    exit, pitching, outfield, infield, catcher, all_dates = (
        [] for _ in range(6))
    list_map = {
        VelocityTypes.EXIT: exit,
        VelocityTypes.PITCHING: pitching,
        VelocityTypes.OUTFIELD: outfield,
        VelocityTypes.INFIELD: infield,
        VelocityTypes.CATCHER: catcher
    }

    for velocity in all_velocities:
        ttype = velocity.ttype.name
        date = velocity.date.strftime('%m/%d/%y')
        velo = velocity.velocity

        list_map[ttype].append((date, velo))
        all_dates.append(date)

    response = {
        "exit": exit,
        "pitching": pitching,
        "outfield": outfield,
        "infield": infield,
        "allDates": all_dates
    }
    
    return JsonResponse(response)


def get_player_pulldowns_with_dates(request):
    """
    Returns all pulldowns (date, velocity) of each type for a given player.
    Also returns a list of all dates for velocities for use with Chart.js.
    """
    player_id = request.GET.get('player_id')
    player = tms.get_player_by_id(player_id)

    three, four, five, six, seven, all_dates = (
        [] for _ in range(6))
    list_map = {
        BallWeights.THREE_OUNCE: three,
        BallWeights.FOUR_OUNCE: four,
        BallWeights.FIVE_OUNCE: five,
        BallWeights.SIX_OUNCE: six,
        BallWeights.SEVEN_OUNCE: seven
    }

    for pulldown in player.pulldowns.all():
        weight = pulldown.ball_weight
        date = pulldown.date.strftime('%m/%d/%y')
        velo = pulldown.velocity

        list_map[weight].append((date, velo))
        all_dates.append(date)

    response = {
        "three": three,
        "four": four,
        "five": five,
        "six": six,
        "seven": seven,
        "allDates": all_dates
    }
    
    return JsonResponse(response)


def get_player_times_with_dates(request):
    """
    Returns all times (date, time) of each type for a given player.
    Also returns a list of all dates for times for use with Chart.js.
    """
    player_id = request.GET.get('player_id')

    sixty_records = pps.get_player_sixty_times(player_id)
    sixty_dates = [time.date.strftime('%m/%d/%y') for time in sixty_records]
    sixty_times = [time.formatted_time() for time in sixty_records]
    sixty_time_return_data = list(zip(sixty_dates, sixty_times))

    response = {
        "sixty": sixty_time_return_data,
        "allDates": sixty_dates
    }
    
    return JsonResponse(response)
