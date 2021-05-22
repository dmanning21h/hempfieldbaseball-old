import datetime

from .models import LiftType, Lift, LiftImprovement
from .models import VelocityType, Velocity, VelocityImprovement
from .models import TimeType, Time, TimeImprovement
from .models import DistanceType, Distance, DistanceImprovement
from .models import BodyWeight, BodyWeightImprovement


# Global for number of Leaderboard players
top = 5


def _get_model_records_by_player_and_type_name(model, player_id, type_name):
    return (
                model.objects
                .filter(player=player_id)
                .filter(ttype__name__iexact=type_name)
                .order_by('date')
            )


def get_player_lifts_by_lift_name(player_id, lift_name):
    return _get_model_records_by_player_and_type_name(Lift,
                                                      player_id,
                                                      lift_name)


def get_player_velocities_by_velocity_name(player_id, velocity_name):
    return _get_model_records_by_player_and_type_name(Velocity,
                                                      player_id,
                                                      velocity_name)


def get_player_distances_by_distance_name(player_id, distance_name):
    return _get_model_records_by_player_and_type_name(Distance,
                                                      player_id,
                                                      distance_name)


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


def _get_latest_model_records(improvement_model, ttype):
    latest_query = (
            improvement_model.objects
            .filter(player__is_active=True)
            .filter(ttype=ttype)
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


def _get_model_leaders(type_model, improvement_model, sorting_key,
                       descending=True):
    leaders = {}
    for ttype in type_model.objects.all():
        latest_records = _get_latest_model_records(improvement_model,
                                                   ttype)
        leaders[ttype.name] = _sort_model_latest_records(latest_records,
                                                         sorting_key,
                                                         descending)
    return leaders


def get_lift_leaders():
    return _get_model_leaders(LiftType,
                              LiftImprovement,
                              lambda l: l.strength_points())


def get_velocity_leaders():
    return _get_model_leaders(VelocityType,
                              VelocityImprovement,
                              lambda v: v.velocity)


def get_time_leaders():
    return _get_model_leaders(TimeType,
                              TimeImprovement,
                              lambda t: t.time,
                              descending=False)


def get_distance_leaders():
    return _get_model_leaders(DistanceType,
                              DistanceImprovement,
                              lambda d: d.distance)


#
# IMPROVEMENT LEADERBOARDS
#


def _get_model_improvement_leaders(type_model, improvement_model,
                                   zero_value=0):
    improvement_leaders = {}
    for ttype in type_model.objects.all():
        improvement_leaders[ttype.name] = (
                improvement_model.objects
                .filter(player__is_active=True)
                .filter(ttype=ttype)
                .filter(improvement__gt=zero_value)
                .order_by('-improvement')
            )[:top]

    return improvement_leaders


def get_lift_improvement_leaders():
    return _get_model_improvement_leaders(LiftType, LiftImprovement)


def get_velocity_improvement_leaders():
    return _get_model_improvement_leaders(VelocityType, VelocityImprovement)


def get_time_improvement_leaders():
    return _get_model_improvement_leaders(TimeType, TimeImprovement,
                                          zero_value=datetime.timedelta(0))


def get_distance_improvement_leaders():
    return _get_model_improvement_leaders(DistanceType, DistanceImprovement)


def get_body_weight_improvement_leaders():
    improvement_leaders = (
        BodyWeightImprovement.objects
        .filter(player__is_active=True)
        .filter(improvement__gt=0)
        .order_by('-improvement')
    )[:top]

    return improvement_leaders
