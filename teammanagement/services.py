from django.shortcuts import get_object_or_404

from teammanagement.models import Team, Player


# Roster
def get_current_team():
    return Team.objects.all().first()


def get_team_by_year(year):
    return get_object_or_404(Team, year=year)


# Individual Player Page
def get_player_from_link(player_link):
    return get_object_or_404(Player.page_object, player_link=player_link)
