from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from . import services as pps
from hempfieldbaseball.teammanagement.models import Player


def get_player_body_weights_with_dates(request):
    """
    Returns all body weights (date, body weight) for a given player.
    """
    player_id = request.GET.get("player_id")
    player = get_object_or_404(Player, pk=player_id)

    body_weights, all_dates = ([] for _ in range(2))
    for body_weight in player.bodyweight_records.all():
        date = body_weight.date.strftime("%m/%d/%y")
        body_weights.append((date, body_weight.weight))
        all_dates.append(date)

    response = {"bodyWeight": body_weights, "allDates": all_dates}

    return JsonResponse(response)


def get_player_lifts_with_dates(request):
    """
    Returns all lifts (date, sets, strength points) of each type for a given player.
    Also returns a list of all dates for lifts for use with Chart.js.
    """
    player_id = request.GET.get("player_id")

    deadlift_records = pps.get_player_deadlift_lifts(player_id)
    deadlift_dates = [lift.date.strftime("%m/%d/%y") for lift in deadlift_records]
    deadlift_return_data = [
        [lift.date.strftime("%m/%d/%y"), lift.strength_points(), lift.sets()]
        for lift in deadlift_records
    ]

    squat_records = pps.get_player_squat_lifts(player_id)
    squat_dates = [lift.date.strftime("%m/%d/%y") for lift in squat_records]
    squat_return_data = [
        [lift.date.strftime("%m/%d/%y"), lift.strength_points(), lift.sets()]
        for lift in squat_records
    ]

    bench_records = pps.get_player_bench_lifts(player_id)
    bench_dates = [lift.date.strftime("%m/%d/%y") for lift in bench_records]
    bench_return_data = [
        [lift.date.strftime("%m/%d/%y"), lift.strength_points(), lift.sets()]
        for lift in bench_records
    ]

    all_dates = sorted(deadlift_dates + squat_dates + bench_dates)

    response = {
        "deadlift": deadlift_return_data,
        "squat": squat_return_data,
        "benchPress": bench_return_data,
        "allDates": all_dates,
    }

    return JsonResponse(response)


def get_player_times_with_dates(request):
    """
    Returns all times (date, time) of each type for a given player.
    Also returns a list of all dates for times for use with Chart.js.
    """
    player_id = request.GET.get("player_id")

    sixty_records = pps.get_player_sixty_times(player_id)
    sixty_dates = [time.date.strftime("%m/%d/%y") for time in sixty_records]
    sixty_times = [time.formatted_time() for time in sixty_records]
    sixty_time_return_data = list(zip(sixty_dates, sixty_times))

    response = {"sixty": sixty_time_return_data, "allDates": sixty_dates}

    return JsonResponse(response)
