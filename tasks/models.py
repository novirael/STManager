from django.db import models
from projects.models import Project


class Task(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    time = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name
