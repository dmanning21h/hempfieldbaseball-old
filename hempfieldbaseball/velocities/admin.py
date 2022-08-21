from django.contrib import admin

from .models import (
    PlyoDrillVelocity,
    Pulldown,
    Velocity,
)


class VelocityAdmin(admin.ModelAdmin):
    list_display = ["date", "player", "position", "velocity"]
    list_filter = ["player", "date", "position"]

    fields = ["player", "date", "position", "velocity"]
    autocomplete_fields = ["player"]


class PulldownAdmin(admin.ModelAdmin):
    list_display = ["date", "player", "ball_weight", "velocity"]
    list_filter = ["player", "date"]

    fields = ["player", "date", "ball_weight", "velocity"]
    autocomplete_fields = ["player"]


class PlyoDrillVelocityAdmin(admin.ModelAdmin):
    list_display = ["date", "player", "drill", "ball_weight", "velocity"]
    list_filter = ["player", "date"]

    fields = ["player", "date", "drill", "ball_weight", "velocity"]
    autocomplete_fields = ["player"]


admin.site.register(Velocity, VelocityAdmin)
admin.site.register(Pulldown, PulldownAdmin)
admin.site.register(PlyoDrillVelocity, PlyoDrillVelocityAdmin)
