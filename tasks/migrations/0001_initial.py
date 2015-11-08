# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('time', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('project', models.ForeignKey(related_name='tasks', to='projects.Project')),
            ],
        ),
    ]
