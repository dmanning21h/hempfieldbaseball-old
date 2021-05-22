from django import template

# from .. import view_data_service as vds


register = template.Library()


# Player Page Inclusion Tags
@register.inclusion_tag('playerprogress/player_partials/lifts.html')
def show_lifts(player):
    pass


def show_velocities(player):
    pass


def show_times(player):
    pass


def show_distances(player):
    pass


def show_body_weights(player):
    pass


# Filter Tags
@register.filter(name='subtract')
def subtract(value, arg):
    return round(value - arg, 2)


@register.filter(name='id_format')
def id_format(value):
    return value.lower().replace(" ", "")


@register.filter(name='time_id_format')
def time_id_format(value):
    semi_format = value.lower().replace(" ", "")
    if "60-yd" in semi_format:
        return semi_format.replace("60-yd", "sixty")
    elif "40-yd" in semi_format:
        return semi_format.replace("40-yd", "forty")
    else:
        return semi_format
