from django.contrib import admin

from .models import TeamSubs


class TeamSubsAdmin(admin.ModelAdmin):
    list_display = (
        'player',
        'period',
        'team',
    )


admin.site.register(TeamSubs, TeamSubsAdmin)
