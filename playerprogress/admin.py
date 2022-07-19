from datetime import timedelta

from django.contrib import admin

from teammanagement.models import Player
from .models import LiftType, Lift, LiftImprovement, LiftSet, StrengthIncrement
from .models import VelocityType, Velocity, VelocityImprovement
from .models import Pulldown
from .models import TimeType, Time, TimeImprovement
from .models import DistanceType, Distance, DistanceImprovement
from .models import BodyWeight, BodyWeightImprovement


class LiftTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']

    fields = ['name', 'order']


class LiftAdmin(admin.ModelAdmin):
    list_display = ('date', 'player', 'ttype', 'set1',
                    'set2', 'set3')
    list_filter = ['player', 'date', 'ttype']

    fieldsets = [
        ('Player', {'fields': ['player', 'date']}),
        ('Lift Information', {'fields':
                              ['ttype']}),
        ('Sets', {'fields': ['set1', 'set2', 'set3']})
    ]
    autocomplete_fields = ['player', 'set1', 'set2', 'set3']

    def save_model(self, request, new_lift, form, change):
        lift_type = new_lift.ttype
        player = new_lift.player

        lift_improvement, created = LiftImprovement.objects.get_or_create(
                                        player=player,
                                        ttype=lift_type)

        if created:
            lift_improvement.baseline = new_lift
            lift_improvement.latest = new_lift
        else:
            if new_lift.date <= lift_improvement.baseline.date:
                lift_improvement.baseline = new_lift
                lift_improvement.improvement = (
                    lift_improvement.latest.strength_points()
                    - new_lift.strength_points())

            elif new_lift.date >= lift_improvement.latest.date:
                lift_improvement.latest = new_lift
                lift_improvement.improvement = (
                    new_lift.strength_points()
                    - lift_improvement.baseline.strength_points())

        lift_improvement.baseline.save()
        lift_improvement.latest.save()
        lift_improvement.save()
        super().save_model(request, new_lift, form, change)


class LiftImprovementAdmin(admin.ModelAdmin):
    list_display = ('player', 'ttype', 'baseline', 'latest')
    list_filter = ['player',]


class LiftSetAdmin(admin.ModelAdmin):
    search_fields = ['weight']
    list_display = ['weight', 'reps']

    fields = ['weight', 'reps']


class StrengthIncrementAdmin(admin.ModelAdmin):
    list_display = ['lift_type', 'lift_set', 'strength_points']
    list_filter = ['lift_type']

    fields = ['lift_type', 'lift_set', 'strength_points']


class VelocityTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']

    fields = ['name', 'order']


class VelocityAdmin(admin.ModelAdmin):
    list_display = ['date', 'player', 'ttype', 'velocity']
    list_filter = ['player', 'date', 'ttype']

    fields = ['player', 'date', 'ttype', 'velocity']
    autocomplete_fields = ['player']

    def save_model(self, request, new_velocity, form, change):
        velocity_type = new_velocity.ttype
        player = new_velocity.player

        velocity_improvement, created = (
            VelocityImprovement.objects.get_or_create(
                                            player=player,
                                            ttype=velocity_type))

        if created:
            velocity_improvement.baseline = new_velocity
            velocity_improvement.latest = new_velocity
        else:
            if new_velocity.date <= velocity_improvement.baseline.date:
                velocity_improvement.baseline = new_velocity
                velocity_improvement.improvement = (
                    velocity_improvement.latest.velocity
                    - new_velocity.velocity)

            elif new_velocity.date >= velocity_improvement.latest.date:
                velocity_improvement.latest = new_velocity
                velocity_improvement.improvement = (
                    new_velocity.velocity
                    - velocity_improvement.baseline.velocity)

        velocity_improvement.baseline.save()
        velocity_improvement.latest.save()
        velocity_improvement.save()
        super().save_model(request, new_velocity, form, change)


class VelocityImprovementAdmin(admin.ModelAdmin):
    list_display = ('player', 'ttype', 'baseline', 'latest')
    list_filter = ['player',]


class PulldownAdmin(admin.ModelAdmin):
    list_display = ['date', 'player', 'ball_weight', 'velocity']
    list_filter = ['player', 'date']

    fields = ['player', 'date', 'ball_weight', 'velocity']
    autocomplete_fields = ['player']


class TimeTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_speed']

    fields = ['name', 'order', 'is_speed']


class TimeAdmin(admin.ModelAdmin):
    list_display = ['date', 'player', 'ttype', 'formatted_time']
    list_filter = ['player', 'date', 'ttype']

    fields = ['player', 'date', 'ttype', 'time']
    autocomplete_fields = ['player']

    def save_model(self, request, new_time, form, change):
        time_type = new_time.ttype
        player = new_time.player

        time_improvement, created = (
            TimeImprovement.objects.get_or_create(
                                            player=player,
                                            ttype=time_type))

        if created:
            time_improvement.baseline = new_time
            time_improvement.latest = new_time
            if new_time.time <= timedelta(seconds=45):
                time_improvement.is_seconds = True
            else:
                time_improvement.is_seconds = False
        else:
            if new_time.date <= time_improvement.baseline.date:
                time_improvement.baseline = new_time
                if time_type.is_speed:
                    time_improvement.improvement = -(
                        time_improvement.latest.time
                        - new_time.time)
                else:
                    time_improvement.improvement = (
                        time_improvement.latest.time
                        - new_time.time)

            elif new_time.date >= time_improvement.latest.date:
                time_improvement.latest = new_time
                if time_type.is_speed:
                    time_improvement.improvement = -(
                        new_time.time
                        - time_improvement.baseline.time)
                else:
                    time_improvement.improvement = (
                        new_time.time
                        - time_improvement.baseline.time)

        time_improvement.baseline.save()
        time_improvement.latest.save()
        time_improvement.save()
        super().save_model(request, new_time, form, change)


class TimeImprovementAdmin(admin.ModelAdmin):
    list_display = ('player', 'ttype', 'baseline', 'latest')
    list_filter = ['player',]


class DistanceTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']

    fields = ['name', 'order']


class DistanceAdmin(admin.ModelAdmin):
    list_display = ['date', 'player', 'ttype', 'distance']
    list_filter = ['player', 'date', 'ttype']

    fields = ['player', 'date', 'ttype', 'distance']
    autocomplete_fields = ['player']

    def save_model(self, request, new_distance, form, change):
        distance_type = new_distance.ttype
        player = new_distance.player

        distance_improvement, created = (
            DistanceImprovement.objects.get_or_create(
                                            player=player,
                                            ttype=distance_type))

        if created:
            distance_improvement.baseline = new_distance
            distance_improvement.latest = new_distance
        else:
            if new_distance.date <= distance_improvement.baseline.date:
                distance_improvement.baseline = new_distance
                distance_improvement.improvement = (
                    distance_improvement.latest.distance
                    - new_distance.distance)

            elif new_distance.date >= distance_improvement.latest.date:
                distance_improvement.latest = new_distance
                distance_improvement.improvement = (
                    new_distance.distance
                    - distance_improvement.baseline.distance)

        distance_improvement.baseline.save()
        distance_improvement.latest.save()
        distance_improvement.save()
        super().save_model(request, new_distance, form, change)


class DistanceImprovementAdmin(admin.ModelAdmin):
    pass


class BodyWeightAdmin(admin.ModelAdmin):
    list_display = ['date', 'player', 'weight']
    list_filter = ['player', 'date']

    fields = ['player', 'date', 'weight']
    autocomplete_fields = ['player']

    def save_model(self, request, new_weight, form, change):
        player = new_weight.player

        weight_improvement, created = (
            BodyWeightImprovement.objects.get_or_create(
                                            player=player))

        if created:
            weight_improvement.baseline = new_weight
            weight_improvement.latest = new_weight
        else:
            if new_weight.date <= weight_improvement.baseline.date:
                weight_improvement.baseline = new_weight
                weight_improvement.improvement = round((
                    weight_improvement.latest.weight
                    - new_weight.weight), 1)

            elif new_weight.date >= weight_improvement.latest.date:
                weight_improvement.latest = new_weight
                weight_improvement.improvement = round((
                    new_weight.weight
                    - weight_improvement.baseline.weight), 1)

        weight_improvement.baseline.save()
        weight_improvement.latest.save()
        weight_improvement.save()
        super().save_model(request, new_weight, form, change)


admin.site.register(LiftType, LiftTypeAdmin)
admin.site.register(Lift, LiftAdmin)
admin.site.register(LiftImprovement, LiftImprovementAdmin)

admin.site.register(LiftSet, LiftSetAdmin)
admin.site.register(StrengthIncrement, StrengthIncrementAdmin)

admin.site.register(VelocityType, VelocityTypeAdmin)
admin.site.register(Velocity, VelocityAdmin)
admin.site.register(VelocityImprovement, VelocityImprovementAdmin)

admin.site.register(Pulldown, PulldownAdmin)

admin.site.register(TimeType, TimeTypeAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(TimeImprovement, TimeImprovementAdmin)

#admin.site.register(DistanceType, DistanceTypeAdmin)
#admin.site.register(Distance, DistanceAdmin)

admin.site.register(BodyWeight, BodyWeightAdmin)
