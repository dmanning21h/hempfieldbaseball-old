from django.contrib import admin

from .models import (
    PlyoDrillVelocity,
    Pulldown,
    VelocityType,
    Velocity,
    VelocityImprovement,
)


class VelocityTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]

    fields = ["name", "order"]


class VelocityAdmin(admin.ModelAdmin):
    list_display = ["date", "player", "ttype", "velocity"]
    list_filter = ["player", "date", "ttype"]

    fields = ["player", "date", "ttype", "velocity"]
    autocomplete_fields = ["player"]

    def save_model(self, request, new_velocity, form, change):
        velocity_type = new_velocity.ttype
        player = new_velocity.player

        velocity_improvement, created = VelocityImprovement.objects.get_or_create(
            player=player, ttype=velocity_type
        )

        if created:
            velocity_improvement.baseline = new_velocity
            velocity_improvement.latest = new_velocity
        else:
            if new_velocity.date <= velocity_improvement.baseline.date:
                velocity_improvement.baseline = new_velocity
                velocity_improvement.improvement = (
                    velocity_improvement.latest.velocity - new_velocity.velocity
                )

            elif new_velocity.date >= velocity_improvement.latest.date:
                velocity_improvement.latest = new_velocity
                velocity_improvement.improvement = (
                    new_velocity.velocity - velocity_improvement.baseline.velocity
                )

        velocity_improvement.baseline.save()
        velocity_improvement.latest.save()
        velocity_improvement.save()
        super().save_model(request, new_velocity, form, change)


class VelocityImprovementAdmin(admin.ModelAdmin):
    list_display = ("player", "ttype", "baseline", "latest")
    list_filter = [
        "player",
    ]


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
admin.site.register(VelocityImprovement, VelocityImprovementAdmin)

admin.site.register(Pulldown, PulldownAdmin)
admin.site.register(PlyoDrillVelocity, PlyoDrillVelocityAdmin)
