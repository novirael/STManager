from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    time = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)

    def __unicode__(self):
        return self.name

