# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailers', '0003_auto_20160604_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='driver',
            field=models.ManyToManyField(to='trailers.Driver'),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='license_num',
            field=models.CharField(max_length=13, null=True, blank=True),
        ),
    ]
