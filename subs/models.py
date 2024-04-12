from django.db import models

from kit.models import Product


class Team(models.Model):

    team_name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.team_name

    def get_friendly_name(self):
        return self.friendly_name


class Team_subs(models.Model):

    class Meta:
        verbose_name_plural = 'Team Subs'

    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_sub = models.BooleanField(default=False, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_product_pk(self):
        return self.product.pk
