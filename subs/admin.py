from django.contrib import admin
from .models import Team, Team_subs


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_team_name',
        'team_name'
    )


class Team_subsAdmin(admin.ModelAdmin):
    readonly_fields = ('product',)


admin.site.register(Team, TeamAdmin)
admin.site.register(Team_subs, Team_subsAdmin)