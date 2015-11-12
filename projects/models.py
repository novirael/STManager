from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True, default=timezone.now)
    finish_date = models.DateField(blank=True, null=True)
    sum_hours_work = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    link_repository = models.URLField(max_length=256, blank=True)

    trello_id = models.CharField(max_length=32, blank=True)
    trello_url = models.URLField(max_length=256, blank=True)

    def __unicode__(self):
        return self.name

    @property
    def total_time(self):
        time = 0
        for task in self.tasks.all():
            time += task.time
        return time
