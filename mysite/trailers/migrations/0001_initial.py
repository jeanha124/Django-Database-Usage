# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=50)),
                ('starting_location', models.CharField(max_length=50)),
                ('transit_location', models.CharField(max_length=50, null=True, blank=True)),
                ('ending_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trailer_index', models.CharField(max_length=10)),
                ('owner', models.CharField(max_length=10, null=True, blank=True)),
                ('vin_num', models.CharField(max_length=20, null=True, blank=True)),
                ('license_num', models.CharField(max_length=6, null=True, blank=True)),
                ('length', models.CharField(max_length=15, null=True, blank=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('manufacturer', models.CharField(max_length=10, null=True, blank=True)),
                ('reg_date', models.CharField(max_length=8, null=True, blank=True)),
                ('create_timestamp', models.DateTimeField(verbose_name=b'date/time')),
                ('delete_timestamp', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='trailer',
            field=models.ForeignKey(to='trailers.Trailer'),
        ),
        migrations.AddField(
            model_name='driver',
            name='trailer',
            field=models.ForeignKey(to='trailers.Trailer'),
        ),
    ]
