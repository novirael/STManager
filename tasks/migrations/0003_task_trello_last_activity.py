# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20151112_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='trello_last_activity',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
