from django.db import models

from kit.models import Product
from checkout.models import Order
from kit.models import Product
from clubadmin.models import Team, Player


class TeamSubs(models.Model):

    class Meta:
        verbose_name_plural = 'Team Subs'

    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='subs', default=1)
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='subs', default=0)
    player = models.ForeignKey(Player, null=False, blank=False, on_delete=models.CASCADE, related_name='subs', default=0)
    period = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE, related_name='subs')
    is_paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=0, default=0)

    def __str__(self):
        return f"{self.player}s Subscription"
    
    def save(self, *args, **kwargs):
        # Caluculate the price based on the period
        self.price = self.period * 50
        super().save(*args, **kwargs)

