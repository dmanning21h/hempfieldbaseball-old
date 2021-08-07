from django import template


register = template.Library()


@register.filter(name='class_standing')
def class_standing(player, year):
    class_standings = ["Senior", "Junior", "Sophomore", "Freshman"]
    year_diff = player.graduation_year - year

    if year_diff < 0:
        return "Graduated"

    return class_standings[year_diff]


@register.filter(name='class_standing_abbr')
def class_standing_abbr(player, year):
    class_standings = ["SR.", "JR.", "SO.", "FR."]
    year_diff = player.graduation_year - year

    if year_diff < 0:
        return "GR."

    return class_standings[year_diff]
