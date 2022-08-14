from django.contrib import admin

from .models import LiftType, Lift, LiftSet, StrengthIncrement
from .models import TimeType, Time
from .models import BodyWeight


class LiftTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]

    fields = ["name", "order"]


class LiftAdmin(admin.ModelAdmin):
    list_display = ("date", "player", "ttype", "set1", "set2", "set3")
    list_filter = ["player", "date", "ttype"]

    fieldsets = [
        ("Player", {"fields": ["player", "date"]}),
        ("Lift Information", {"fields": ["ttype"]}),
        ("Sets", {"fields": ["set1", "set2", "set3"]}),
    ]
    autocomplete_fields = ["player", "set1", "set2", "set3"]


class LiftSetAdmin(admin.ModelAdmin):
    search_fields = ["weight"]
    list_display = ["weight", "reps"]

    fields = ["weight", "reps"]


class StrengthIncrementAdmin(admin.ModelAdmin):
    list_display = ["lift_type", "lift_set", "strength_points"]
    list_filter = ["lift_type"]

    fields = ["lift_type", "lift_set", "strength_points"]


class TimeTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "order", "is_speed"]

    fields = ["name", "order", "is_speed"]


class TimeAdmin(admin.ModelAdmin):
    list_display = ["date", "player", "ttype", "formatted_time"]
    list_filter = ["player", "date", "ttype"]

    fields = ["player", "date", "ttype", "time"]
    autocomplete_fields = ["player"]


class DistanceTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]

    fields = ["name", "order"]


class DistanceAdmin(admin.ModelAdmin):
    list_display = ["date", "player", "ttype", "distance"]
    list_filter = ["player", "date", "ttype"]

    fields = ["player", "date", "ttype", "distance"]
    autocomplete_fields = ["player"]


class BodyWeightAdmin(admin.ModelAdmin):
    list_display = ["date", "player", "weight"]
    list_filter = ["player", "date"]

    fields = ["player", "date", "weight"]
    autocomplete_fields = ["player"]


admin.site.register(LiftType, LiftTypeAdmin)
admin.site.register(Lift, LiftAdmin)

admin.site.register(LiftSet, LiftSetAdmin)
admin.site.register(StrengthIncrement, StrengthIncrementAdmin)

admin.site.register(TimeType, TimeTypeAdmin)
admin.site.register(Time, TimeAdmin)

admin.site.register(BodyWeight, BodyWeightAdmin)
