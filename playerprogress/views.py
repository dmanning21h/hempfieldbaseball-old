from django.http import JsonResponse
from django.shortcuts import render

from . import services as pps
from .enums import VelocityTypes


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
    player_id = player_id = request.GET.get('player_id')

    body_weight_records = pps.get_player_body_weights(player_id)
    body_weight_dates = [body_weight.date.strftime('%m/%d/%y') for body_weight in body_weight_records]
    body_weights = [body_weight.weight for body_weight in body_weight_records]
    body_weight_return_data = list(zip(body_weight_dates, body_weights))

    response = {
        "bodyWeight": body_weight_return_data,
        "allDates": body_weight_dates
    }

    return JsonResponse(response)


def get_player_lifts_with_dates(request):
    """
    Returns all lifts (date, sets, strength points) of each type for a given player.
    Also returns a list of all dates for lifts for use with Chart.js.
    """
    player_id = player_id = request.GET.get('player_id')

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
    player_id = player_id = request.GET.get('player_id')

    exit_velocity_records = pps.get_player_exit_velocities(player_id)
    exit_velocity_dates = [velocity.date.strftime('%m/%d/%y') for velocity in exit_velocity_records]
    exit_velocities = [velocity.velocity for velocity in exit_velocity_records]
    exit_velocity_return_data = list(zip(exit_velocity_dates, exit_velocities))

    pitching_velocity_records = pps.get_player_pitching_velocities(player_id)
    pitching_velocity_dates = [velocity.date.strftime('%m/%d/%y') for velocity in pitching_velocity_records]
    pitching_velocities = [velocity.velocity for velocity in pitching_velocity_records]
    pitching_velocity_return_data = list(zip(pitching_velocity_dates, pitching_velocities))

    outfield_velocity_records = pps.get_player_outfield_velocities(player_id)
    outfield_velocity_dates = [velocity.date.strftime('%m/%d/%y') for velocity in outfield_velocity_records]
    outfield_velocities = [velocity.velocity for velocity in outfield_velocity_records]
    outfield_velocity_return_data = list(zip(outfield_velocity_dates, outfield_velocities))

    infield_velocity_records = pps.get_player_infield_velocities(player_id)
    infield_velocity_dates = [velocity.date.strftime('%m/%d/%y') for velocity in infield_velocity_records]
    infield_velocities = [velocity.velocity for velocity in infield_velocity_records]
    infield_velocity_return_data = list(zip(infield_velocity_dates, infield_velocities))

    all_dates = sorted(exit_velocity_dates + pitching_velocity_dates + outfield_velocity_dates + infield_velocity_dates) 

    response = {
        "exit": exit_velocity_return_data,
        "pitching": pitching_velocity_return_data,
        "outfield": outfield_velocity_return_data,
        "infield": infield_velocity_return_data,
        "allDates": all_dates
    }
    
    return JsonResponse(response)


def get_player_times_with_dates(request):
    """
    Returns all times (date, time) of each type for a given player.
    Also returns a list of all dates for times for use with Chart.js.
    """
    player_id = player_id = request.GET.get('player_id')

    sixty_records = pps.get_player_sixty_times(player_id)
    sixty_dates = [time.date.strftime('%m/%d/%y') for time in sixty_records]
    sixty_times = [time.formatted_time() for time in sixty_records]
    sixty_time_return_data = list(zip(sixty_dates, sixty_times))

    response = {
        "sixty": sixty_time_return_data,
        "allDates": sixty_dates
    }
    
    return JsonResponse(response)
