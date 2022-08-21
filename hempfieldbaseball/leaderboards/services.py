from django.db.models import Prefetch

from hempfieldbaseball.teammanagement.models import Player
from hempfieldbaseball.velocities.models import Velocity


# Global for number of Leaderboard players
top = 15


#
# IMPROVEMENT LEADERBOARDS
#
def get_velocity_improvement_leaders(position):
    improvement_leaders = []

    for player in Player.active_players.prefetch_related(
        Prefetch(
            "velocity_records",
            queryset=Velocity.objects.filter(position=position),
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
    improvement_leaders = []

    for player in Player.active_players.prefetch_related(
        Prefetch("bodyweight_records"),
    ).all():
        body_weights = list(player.bodyweight_records.all())
        if len(body_weights) > 1:
            baseline = body_weights[0]
            latest = body_weights[-1]
            improvement = round(latest.weight - baseline.weight, 1)

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
