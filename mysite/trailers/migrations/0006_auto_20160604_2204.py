# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailers', '0005_remove_driver_trailer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='id',
        ),
        migrations.AlterField(
            model_name='location',
            name='trailer',
            field=models.ForeignKey(primary_key=True, serialize=False, to='trailers.Trailer'),
        ),
    ]
