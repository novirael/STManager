from django.db import models


class Task(models.Model):
    project = models.ForeignKey('projects.Project')
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    time = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name
