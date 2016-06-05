# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trailers', '0002_auto_20160603_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='location_name',
        ),
        migrations.AddField(
            model_name='location',
            name='create_timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='trailer_index',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
