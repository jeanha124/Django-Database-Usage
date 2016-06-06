# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='license_num',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
