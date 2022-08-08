from .models import Lift, Time, BodyWeight
from .enums import LiftTypes, TimeTypes


# Lifting
def get_player_deadlift_lifts(player_id):
    return _get_player_lifts_by_lift_name(player_id, LiftTypes.DEADLIFT)


def get_player_squat_lifts(player_id):
    return _get_player_lifts_by_lift_name(player_id, LiftTypes.BACK_SQUAT)


def get_player_bench_lifts(player_id):
    return _get_player_lifts_by_lift_name(player_id, LiftTypes.BENCH_PRESS)


# Times
def get_player_sixty_times(player_id):
    return _get_player_times_by_time_name(player_id, TimeTypes.SIXTY_YARD_DASH)


# Misc
def get_player_body_weights(player_id):
    body_weight_data = BodyWeight.objects.filter(player=player_id).order_by("date")

    return body_weight_data


# More General Model Functions
def _get_player_lifts_by_lift_name(player_id, lift_name):
    return _get_model_records_by_player_id_and_ttype_name(Lift, player_id, lift_name)


def _get_player_times_by_time_name(player_id, time_name):
    return _get_model_records_by_player_id_and_ttype_name(Time, player_id, time_name)


# Most General Model Helper Functions
def _get_model_records_by_player_id_and_ttype_name(model, player_id, ttype_name):
    return (
        model.objects.filter(player=player_id)
        .filter(ttype__name=ttype_name)
        .order_by("date")
    )
