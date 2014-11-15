from django.db import models
from datetime import datetime


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True, default=datetime.now())
    finish_date = models.DateField(blank=True, null=True)
    sum_hours_work = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    link_repository = models.URLField(max_length=256)

    def __unicode__(self):
        return self.name
