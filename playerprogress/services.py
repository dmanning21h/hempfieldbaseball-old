import datetime as dt

from .models import LiftType, Lift
from .models import VelocityType, Velocity
from .models import TimeType, Time
from .models import DistanceType, Distance
from .models import BodyWeight, BodyWeightImprovement
from .enums import LiftType, VelocityType, TimeType


# Global for number of Leaderboard players
top = 10


# Lifting
def get_player_deadlift_lifts(player_id):
    return _get_player_lifts_by_lift_name(player_id, LiftType.DEADLIFT)

def get_player_squat_lifts(player_id):
    return _get_player_lifts_by_lift_name(player_id, LiftType.BACK_SQUAT)

def get_player_bench_lifts(player_id):
    return _get_player_lifts_by_lift_name(player_id, LiftType.BENCH_PRESS)


# Velocities
def get_player_exit_velocities(player_id):
    return _get_player_velocities_by_velocity_name(player_id, VelocityType.EXIT)

def get_player_pitching_velocities(player_id):
    return _get_player_velocities_by_velocity_name(player_id, VelocityType.PITCHING)

def get_player_outfield_velocities(player_id):
    return _get_player_velocities_by_velocity_name(player_id, VelocityType.OUTFIELD)

def get_player_infield_velocities(player_id):
    return _get_player_velocities_by_velocity_name(player_id, VelocityType.INFIELD)


# Times
def get_player_sixty_times(player_id):
    return _get_player_times_by_time_name(player_id, TimeType.SIXTY_YARD_DASH)


# Misc
def get_player_body_weights(player_id):
    body_weight_data = (
            BodyWeight.objects
            .filter(player=player_id)
        )

    return body_weight_data


# More General Model Functions
def _get_player_lifts_by_lift_name(player_id, lift_name):
    return _get_model_records_by_player_id_and_ttype_name(Lift, player_id, lift_name)

def _get_player_velocities_by_velocity_name(player_id, velocity_name):
    return _get_model_records_by_player_id_and_ttype_name(Velocity, player_id, velocity_name)

def _get_player_times_by_time_name(player_id, time_name):
    return _get_model_records_by_player_id_and_ttype_name(Time, player_id, time_name)


# Most General Model Helper Functions
def _get_model_records_by_player_id_and_ttype_name(model, player_id, ttype_name):
    return (
            model.objects
            .filter(player=player_id)
            .filter(ttype__name=ttype_name)
        )


#
# PERFORMANCE LEADERBOARDS
#
def _get_latest_model_records(ttype):
    latest_query = (
            ttype.improvements
            .filter(player__is_active=True)
            .only('latest')
        )
    latest_records = [x.latest for x in latest_query]

    return latest_records


def _sort_model_latest_records(latest_records, sorting_key, descending):
    return sorted(
            latest_records,
            key=sorting_key,
            reverse=descending
        )[:top]


def _get_model_leaders(type_model, sorting_key, descending=True):
    leaders = {}
    for ttype in type_model.objects.all():
        latest_records = _get_latest_model_records(ttype)
        if descending == False:
            if ttype.is_speed == False:
                leaders[ttype.name] = _sort_model_latest_records(latest_records,
                                                                 sorting_key,
                                                                 True)
                continue

        leaders[ttype.name] = _sort_model_latest_records(latest_records,
                                                         sorting_key,
                                                         descending)
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
def _get_model_improvement_leaders(type_model, zero_value=0):
    improvement_leaders = {}
    for ttype in type_model.objects.all():
        improvement_leaders[ttype.name] = (
                ttype.improvements
                .filter(player__is_active=True)
                .filter(improvement__gt=zero_value)
                .order_by('-improvement')
            )[:top]

    return improvement_leaders


def get_lift_improvement_leaders():
    return _get_model_improvement_leaders(LiftType)


def get_velocity_improvement_leaders():
    return _get_model_improvement_leaders(VelocityType)


def get_time_improvement_leaders():
    return _get_model_improvement_leaders(TimeType, zero_value=dt.timedelta(0))


def get_distance_improvement_leaders():
    return _get_model_improvement_leaders(DistanceType)


def get_body_weight_improvement_leaders():
    top = 10

    improvement_leaders = (
        BodyWeightImprovement.objects
        .filter(player__is_active=True)
        .filter(improvement__gt=0)
        .order_by('-improvement')
    )[:top]

    return improvement_leaders
