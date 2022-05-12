from django.shortcuts import get_object_or_404

from teammanagement.models import Team, Player


# Roster
def get_current_team():
    return Team.page_objects.all().first()


def get_team_by_year(year):
    return get_object_or_404(Team.page_objects, year=year)


# Individual Player Page
def get_player_from_link(player_link):
    return get_object_or_404(Player.page_objects, player_link=player_link)
