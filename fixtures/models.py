from django.db import models
from django.core.validators import MinValueValidator
from datetime import date


class Fixture(models.Model):

    team = models.CharField(max_length=50, null=False, blank=False)
    opponent = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(
        validators=[MinValueValidator(limit_value=date.today)],
        null=False, blank=False)
    time = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
