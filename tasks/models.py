from django.db import models
from projects.models import Project


class Task(models.Model):
    project = models.ForeignKey(Project, related_name="tasks")
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    time = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True, blank=True)

    trello_id = models.CharField(max_length=32, blank=True)
    trello_url = models.URLField(max_length=256, blank=True)

    def __unicode__(self):
        return self.name
