from django.contrib import admin
from .models import Team, News, NewsCategory


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_team_name',
        'team_name'
    )


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_news_name',
    )


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'news_category',
        'date'
    )
    ordering = ('date',)


admin.site.register(Team, TeamAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)