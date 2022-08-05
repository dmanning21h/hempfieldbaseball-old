from .models import LiftType, Lift
from .models import TimeType, Time
from .models import DistanceType
from .models import BodyWeight, BodyWeightImprovement
from .enums import LiftTypes, TimeTypes

from hempfieldbaseball.velocities.models import VelocityType


# Global for number of Leaderboard players
top = 15


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


#
# PERFORMANCE LEADERBOARDS
#
def _get_latest_model_records(ttype):
    latest_query = ttype.improvements.filter(player__is_active=True).only("latest")
    latest_records = [x.latest for x in latest_query]

    return latest_records


def _sort_model_latest_records(latest_records, sorting_key, descending):
    return sorted(latest_records, key=sorting_key, reverse=descending)[:top]


def _get_model_leaders(type_model, sorting_key, descending=True):
    leaders = {}
    for ttype in type_model.objects.all():
        latest_records = _get_latest_model_records(ttype)
        if descending is False:
            if ttype.is_speed is False:
                leaders[ttype.name] = _sort_model_latest_records(
                    latest_records, sorting_key, True
                )
                continue

        leaders[ttype.name] = _sort_model_latest_records(
            latest_records, sorting_key, descending
        )
    return leaders


def get_lift_leaders():
    return _get_model_leaders(LiftType, lambda l: l.strength_points())


def get_velocity_leaders():
    return _get_model_leaders(VelocityType, lambda v: v.velocity)


def get_time_leaders():
    return _get_model_leaders(TimeType, lambda t: t.time, descending=False)


def get_distance_leaders():
    return _get_model_leaders(DistanceType, lambda d: d.distance)


#
# IMPROVEMENT LEADERBOARDS
#
def get_velocity_improvement_leaders(velocity_name):
    return _get_model_improvement_leaders(VelocityType, velocity_name)


def _get_model_improvement_leaders(type_model, type_model_name, zero_value=0):
    ttype = type_model.leaderboard_objects.get(name=type_model_name)
    return (
        ttype.improvements.filter(player__is_active=True)
        .filter(improvement__gt=zero_value)
        .order_by("-improvement")
    )[:top]


def get_body_weight_improvement_leaders():
    improvement_leaders = (
        BodyWeightImprovement.leaderboard_objects.filter(player__is_active=True)
        .filter(improvement__gt=0)
        .order_by("-improvement")
    )[:top]

    return improvement_leaders


# def get_lift_improvement_leaders():
#    return _get_model_improvement_leaders(LiftType)


# def get_time_improvement_leaders():
#    return _get_model_improvement_leaders(TimeType, zero_value=dt.timedelta(0))


# def get_distance_improvement_leaders():
#    return _get_model_improvement_leaders(DistanceType)
