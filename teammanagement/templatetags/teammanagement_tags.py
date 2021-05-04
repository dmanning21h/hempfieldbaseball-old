from django import template


register = template.Library()


@register.inclusion_tag("teammanagement/partials/player_header.html",
                        takes_context=True)
def show_player_header(context):
    return {'player': context['player']}


@register.inclusion_tag("teammanagement/partials/player_lifts.html",
                        takes_context=True)
def show_player_lifts(context):
    return {'lift_data': context['lift_data']}


@register.inclusion_tag("teammanagement/partials/player_velocities.html",
                        takes_context=True)
def show_player_velocities(context):
    return {'velocity_data': context['velocity_data']}


@register.inclusion_tag("teammanagement/partials/player_times.html",
                        takes_context=True)
def show_player_times(context):
    return {'time_data': context['time_data']}


@register.inclusion_tag("teammanagement/partials/player_distances.html",
                        takes_context=True)
def show_player_distances(context):
    return {'distance_data': context['distance_data']}


@register.inclusion_tag("teammanagement/partials/player_misc.html",
                        takes_context=True)
def show_player_misc(context):
    return {'body_weights': context['body_weights']}
