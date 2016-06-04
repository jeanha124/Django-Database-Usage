# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailer',
            name='create_timestamp',
        ),
        migrations.RemoveField(
            model_name='trailer',
            name='delete_timestamp',
        ),
    ]
