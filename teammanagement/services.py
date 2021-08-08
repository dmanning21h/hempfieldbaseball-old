from django.shortcuts import get_object_or_404

from teammanagement.models import Team, TeamPlayer, Player


# Roster
def get_current_team():
    return Team.objects.all().first()


def get_team_by_year(year):
    return get_object_or_404(Team, year=year)


# Individual Player Page
def get_player_id_from_link(player_link):
    player = get_object_or_404(Player, player_link=player_link)

    return player.player_id


def get_latest_team_player_by_player_id(player_id):
    return (
            TeamPlayer.objects
            .filter(info_id=player_id)
            .order_by('team__year')
            .last()
        )
