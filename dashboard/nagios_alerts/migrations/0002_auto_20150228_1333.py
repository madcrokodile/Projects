# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nagios_alerts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='carrot',
            field=models.CharField(max_length=200, default='mew'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servers',
            name='focus',
            field=models.CharField(max_length=200, default='pew'),
            preserve_default=False,
        ),
    ]
