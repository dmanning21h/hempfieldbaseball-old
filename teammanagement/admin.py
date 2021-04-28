from django.contrib import admin

from .models import Team, Player, Coach, TeamPlayer, TeamCoach
from .models import Position, CoachRole, Height


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'graduation_year')
    list_filter = ['graduation_year']

    fieldsets = [
        ('Personal', {'fields': ['first_name', 'last_name',
                                 'graduation_year']}),
        ('Roster Info', {'fields':
                         ['bats', 'throws']}),
        ('Unique Player Page Link', {'fields': ['player_link']})
    ]


class TeamPlayerInline(admin.TabularInline):
    model = TeamPlayer
    extra = 0


class CoachAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


class TeamCoachInline(admin.TabularInline):
    model = TeamCoach
    extra = 0


class TeamAdmin(admin.ModelAdmin):
    list_display = ('year',)

    inlines = (TeamPlayerInline, TeamCoachInline)


admin.site.register(Player, PlayerAdmin)
admin.site.register(Position)
admin.site.register(Coach, CoachAdmin)
admin.site.register(CoachRole)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamPlayer)
admin.site.register(TeamCoach)
admin.site.register(Height)
