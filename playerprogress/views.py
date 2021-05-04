from django.http import JsonResponse
from django.shortcuts import render

from . import services as pps


def get_player_data_and_dates(request):
    player_id = request.GET.get('player_id')
    data_type = request.GET.get('data_type')

    if data_type == "lift":
        lift_name = request.GET.get('metric_name')
        records = pps.get_player_lifts_by_lift_name(player_id, lift_name)
        data = [lift.strength_points() for lift in records]
        dates = [lift.date.strftime('%m/%d/%y') for lift in records]

    elif data_type == "velocity":
        velo_name = request.GET.get('metric_name')
        records = pps.get_player_velocities_by_velocity_name(player_id,
                                                             velo_name)
        data = [velo.velocity for velo in records]
        dates = [velo.date.strftime('%m/%d/%y') for velo in records]

    elif data_type == "time":
        pass

    elif data_type == "distance":
        distance_name = request.GET.get('metric_name')
        records = pps.get_player_distances_by_distance_name(player_id,
                                                            distance_name)
        data = [dist.distance for dist in records]
        dates = [dist.date.strftime('%m/%d/%y') for dist in records]

    elif data_type == "weight":
        records = pps.get_all_player_body_weights(player_id)
        data = [bw.weight for bw in records]
        dates = [bw.date.strftime('%m/%d/%y') for bw in records]

    data = {
        'data': data,
        'dates': dates
    }
    return JsonResponse(data)


def get_player_lift_data_and_dates(request):
    player_id = request.GET.get('player_id')
    lift_name = request.GET.get('lift_name')

    records = pps.get_player_lifts_by_lift_name(player_id, lift_name)
    data = [lift.strength_points() for lift in records]
    dates = [lift.date.strftime('%m/%d/%y') for lift in records]

    response = {
        'data': data,
        'dates': dates
    }
    return JsonResponse(response)


def leaderboards(request):
    lift_data_exists = pps.does_lift_data_exist()
    velocity_data_exists = pps.does_velocity_data_exist()
    time_data_exists = pps.does_time_data_exist()
    distance_data_exists = pps.does_distance_data_exist()
    body_weight_data_exists = pps.does_body_weight_data_exist()

    context = {
        'lift_data_exists':
            lift_data_exists,
        'velocity_data_exists':
            velocity_data_exists,
        'time_data_exists':
            time_data_exists,
        'distance_data_exists':
            distance_data_exists,
        'body_weight_data_exists':
            body_weight_data_exists
    }

    return render(request, 'playerprogress/leaderboards.html',
                  context)


def resources(request):
    context = {}

    return render(request, 'playerprogress/resources.html', context)


def lifting_performance_leaderboards(request):
    lift_leader_data = pps.get_lift_leaders()

    context = {
        'lift_leader_data': lift_leader_data,
    }

    return render(request, 'playerprogress/performance/lifting.html',
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


def distance_performance_leaderboards(request):
    distance_leader_data = pps.get_distance_leaders()

    context = {
        'distance_leader_data': distance_leader_data,
    }

    return render(request, 'playerprogress/performance/distance.html',
                  context)


def misc_performance_leaderboards(request):

    context = {}

    return render(request, 'playerprogress/performance/misc.html', context)


def lifting_improvement_leaderboards(request):
    lift_improvement_leader_data = pps.get_lift_improvement_leaders()

    context = {
        'lift_improvement_leader_data': lift_improvement_leader_data,
    }

    return render(request, 'playerprogress/improvement/lifting.html',
                  context)


def velocity_improvement_leaderboards(request):
    velocity_improvement_leader_data = pps.get_velocity_improvement_leaders()

    context = {
        'velocity_improvement_leader_data': velocity_improvement_leader_data,
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


def distance_improvement_leaderboards(request):
    distance_improvement_leader_data = pps.get_distance_improvement_leaders()

    context = {
        'distance_improvement_leader_data': distance_improvement_leader_data
    }

    return render(request, 'playerprogress/improvement/distance.html',
                  context)


def misc_improvement_leaderboards(request):
    body_weight_improvement_leaders = pps.get_body_weight_improvement_leaders()

    context = {
        'body_weight_improvement_leaders':
            body_weight_improvement_leaders,
    }

    return render(request, 'playerprogress/improvement/misc.html', context)
