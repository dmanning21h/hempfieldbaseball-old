from django.contrib import admin

from .models import Team, Player, Coach, TeamPlayer, TeamCoach
from .models import Position, CoachRole, Height


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['last_name']
    list_display = ('full_name', 'graduation_year', 'is_active')
    list_filter = ['graduation_year']

    fieldsets = [
        ('Personal', {'fields': ['first_name', 'last_name',
                                 'graduation_year']}),
        ('Roster Info', {'fields':
                         ['bats', 'throws']}),
        ('Unique Player Page Link', {'fields': ['player_link']}),
        ('Is player active?', {'fields': ['is_active']})
    ]
    
    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term,
        )

        if search_term:
            queryset &= self.model.objects.filter(is_active=True)
        
        return queryset, may_have_duplicates


class TeamPlayerInline(admin.TabularInline):
    model = TeamPlayer
    extra = 0

    autocomplete_fields = ('personal_info',)


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
