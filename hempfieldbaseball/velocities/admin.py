from django.contrib import admin

from .models import (
    PlyoDrillVelocity,
    Pulldown,
    VelocityType,
    Velocity,
)


class VelocityTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]

    fields = ["name", "order"]


class VelocityAdmin(admin.ModelAdmin):
    list_display = ["date", "player", "ttype", "velocity"]
    list_filter = ["player", "date", "ttype"]

    fields = ["player", "date", "ttype", "velocity"]
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


admin.site.register(VelocityType, VelocityTypeAdmin)
admin.site.register(Velocity, VelocityAdmin)

admin.site.register(Pulldown, PulldownAdmin)
admin.site.register(PlyoDrillVelocity, PlyoDrillVelocityAdmin)
