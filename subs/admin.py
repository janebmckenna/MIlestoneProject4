from django.contrib import admin

from .models import  Team_subs
from clubadmin.models import Team


class Team_subsAdmin(admin.ModelAdmin):
    list_display = (
        'player_name',
        'period',
    )


admin.site.register(Team_subs, Team_subsAdmin)