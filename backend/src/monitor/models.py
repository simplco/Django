from django.db import models

# Create your models here.


class Monitor(models.Model):
    date = models.DateTimeField('date published')
    kw = models.FloatField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    voltage = models.FloatField(null=True, blank=True)
    current = models.FloatField(null=True, blank=True)
