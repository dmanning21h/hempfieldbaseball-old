import datetime as dt

from .models import Player
from .models import LiftType, Lift, LiftImprovement
from .models import VelocityType, Velocity, VelocityImprovement
from .models import TimeType, Time, TimeImprovement
from .models import DistanceType, Distance, DistanceImprovement
from .models import BodyWeight, BodyWeightImprovement


# Global for number of Leaderboard players
top = 5


def get_player_lifts_by_lift_name(player_id, lift_name):
    return (
        Player.objects.get(player_id=player_id)
        .lifts.filter(ttype__name=lift_name)
        .order_by('date')
    )


def get_player_velocities_by_velocity_name(player_id, velocity_name):
    return (
        Player.objects.get(player_id=player_id)
        .velocities.filter(ttype__name=velocity_name)
        .order_by('date')
    )


def get_player_distances_by_distance_name(player_id, distance_name):
    return (
        Player.objects.get(player_id=player_id)
        .distances.filter(ttype__name=distance_name)
        .order_by('date')
    )


def _model_records_exist(model):
    if len(model.objects.all()) > 0:
        return True
    else:
        return False


def does_lift_data_exist():
    return _model_records_exist(Lift)


def does_velocity_data_exist():
    return _model_records_exist(Velocity)


def does_time_data_exist():
    return _model_records_exist(Time)


def does_distance_data_exist():
    return _model_records_exist(Distance)


def does_body_weight_data_exist():
    return _model_records_exist(BodyWeight)


# Dict grouping with type name as key
def _get_model_records_by_player(type_model, model, player_id):
    records = {}
    for ttype in type_model.objects.all():
        single_type_data = (
                model.objects
                .filter(player=player_id)
                .filter(ttype=ttype)
                .order_by('date')
            )
        records[ttype.name] = single_type_data

    return records


def get_all_player_lifts(player_id):
    return _get_model_records_by_player(LiftType, Lift, player_id)


def get_all_player_velocities(player_id):
    return _get_model_records_by_player(VelocityType, Velocity, player_id)


def get_all_player_times(player_id):
    return _get_model_records_by_player(TimeType, Time, player_id)


def get_all_player_distances(player_id):
    return _get_model_records_by_player(DistanceType, Distance, player_id)


def get_all_player_body_weights(player_id):
    body_weight_data = (
            BodyWeight.objects
            .filter(player=player_id)
            .order_by('date')
        )

    return body_weight_data


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
    improvement_leaders = (
        BodyWeightImprovement.objects
        .filter(player__is_active=True)
        .filter(improvement__gt=0)
        .order_by('-improvement')
    )[:top]

    return improvement_leaders
