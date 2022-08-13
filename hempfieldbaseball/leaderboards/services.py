from django.db.models import Prefetch

from hempfieldbaseball.playerprogress.models import BodyWeightImprovement, TimeType
from hempfieldbaseball.teammanagement.models import Player
from hempfieldbaseball.velocities.models import Velocity, VelocityType


# Global for number of Leaderboard players
top = 15


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


def get_velocity_leaders():
    return _get_model_leaders(VelocityType, lambda v: v.velocity)


def get_time_leaders():
    return _get_model_leaders(TimeType, lambda t: t.time, descending=False)


#
# IMPROVEMENT LEADERBOARDS
#
def get_velocity_improvement_leaders(velocity_name):
    improvement_leaders = []

    for player in Player.active_players.prefetch_related(
        Prefetch(
            "velocity_records",
            queryset=Velocity.objects.select_related("ttype").filter(
                ttype__name=velocity_name
            ),
        )
    ).all():
        velocities = list(player.velocity_records.all())
        if len(velocities) > 1:
            baseline = velocities[0]
            latest = velocities[-1]
            improvement = latest.velocity - baseline.velocity

            if improvement >= 0:
                improvement_leaders.append(
                    {
                        "player": player,
                        "improvement": improvement,
                        "baseline": baseline,
                        "latest": latest,
                    }
                )

    return sorted(improvement_leaders, key=lambda l: l["improvement"], reverse=True)


def get_body_weight_improvement_leaders():
    improvement_leaders = (
        BodyWeightImprovement.leaderboard_objects.filter(player__is_active=True)
        .filter(improvement__gt=0)
        .order_by("-improvement")
    )[:top]

    return improvement_leaders
