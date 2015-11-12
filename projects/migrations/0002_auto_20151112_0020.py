# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='trello_id',
            field=models.CharField(max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='trello_url',
            field=models.URLField(max_length=256, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='link_repository',
            field=models.URLField(max_length=256, blank=True),
        ),
    ]
