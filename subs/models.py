from django.db import models

from kit.models import Product
from checkout.models import Order
from clubadmin.models import Team


class Team_subs(models.Model):

    class Meta:
        verbose_name_plural = 'Team Subs'

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='subs', default=0)
    player_name = models.CharField(max_length=80, null=True, blank=True)
    period = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    def __str__(self):
        return self.player_name

    def get_product_pk(self):
        return self.product.pk
