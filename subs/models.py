from django.db import models

from kit.models import Product
from checkout.models import Order


class Team(models.Model):

    team_name = models.CharField(max_length=254)
    friendly_team_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.team_name

    def get_friendly_name(self):
        return self.friendly_name


class Team_subs(models.Model):

    class Meta:
        verbose_name_plural = 'Team Subs'

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='subs', default=0)
    team = models.ForeignKey('Team', null=False, blank=False, on_delete=models.CASCADE, default=0)
    player_name = models.CharField(max_length=80, null=True, blank=True)
    period = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    def __str__(self):
        return self.player_name

    def get_product_pk(self):
        return self.product.pk
