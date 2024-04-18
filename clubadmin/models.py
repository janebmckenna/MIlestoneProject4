from django.db import models

from kit.models import Product


class Team(models.Model):

    team_name = models.CharField(max_length=254)
    friendly_team_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.team_name

    def get_friendly_name(self):
        return self.friendly_team_name


class NewsCategory(models.Model):

    class Meta:
        verbose_name_plural = 'News Categories'

    news_name = models.CharField(max_length=50)
    friendly_news_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.news_name

    def get_news_friendly_name(self):
        return self.friendly_news_name


class News(models.Model):

    class Meta:
        verbose_name_plural = 'News'

    news_category = models.ForeignKey('NewsCategory', null=True, blank=True, on_delete=models.SET_NULL)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254, null=False, blank=False)
    news = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title