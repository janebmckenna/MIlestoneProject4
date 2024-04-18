from django.contrib import admin

from .models import  TeamSubs
from clubadmin.models import Team


class TeamSubsAdmin(admin.ModelAdmin):
    list_display = (
        'player',
        'period',
    )


admin.site.register(TeamSubs, TeamSubsAdmin)