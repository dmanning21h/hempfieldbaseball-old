from django.contrib import admin

from .models import AlumniPlayer, AlumniClass


class AlumniPlayerInline(admin.TabularInline):
    model = AlumniPlayer
    extra = 0


class AlumniClassAdmin(admin.ModelAdmin):
    list_display = ('year',)

    inlines = (AlumniPlayerInline,)


admin.site.register(AlumniClass, AlumniClassAdmin)
admin.site.register(AlumniPlayer)
