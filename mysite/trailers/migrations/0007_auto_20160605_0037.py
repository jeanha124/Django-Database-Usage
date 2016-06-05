# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trailers', '0006_auto_20160604_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitedLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.PositiveIntegerField(verbose_name=b'Visited Location Type', choices=[(0, b'start'), (1, b'transit'), (2, b'end')])),
                ('visited_datetime', models.DateTimeField(verbose_name=b'Location Visit Datetime')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Datetime')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Update Datetime')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is Active')),
            ],
        ),
        migrations.RemoveField(
            model_name='location',
            name='create_timestamp',
        ),
        migrations.RemoveField(
            model_name='location',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='location',
            name='ending_location',
        ),
        migrations.RemoveField(
            model_name='location',
            name='starting_location',
        ),
        migrations.RemoveField(
            model_name='location',
            name='trailer',
        ),
        migrations.RemoveField(
            model_name='location',
            name='transit_location',
        ),
        migrations.AddField(
            model_name='driver',
            name='create_datetime',
            field=models.DateTimeField(verbose_name=b'Create Datetime', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'Is Active'),
        ),
        migrations.AddField(
            model_name='driver',
            name='update_datetime',
            field=models.DateTimeField(verbose_name=b'Update Datetime', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='address_1',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Address 1', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='address_2',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Address 2', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name=b'City', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='create_datetime',
            field=models.DateTimeField(verbose_name=b'Create Datetime', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'Is Active'),
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Location Name', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='phone',
            field=models.CharField(max_length=16, null=True, verbose_name=b'Phone Number', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=100, null=True, verbose_name=b'State', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='update_datetime',
            field=models.DateTimeField(verbose_name=b'Update Datetime', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='zipcode',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Zip Code', blank=True),
        ),
        migrations.AddField(
            model_name='trailer',
            name='create_datetime',
            field=models.DateTimeField(verbose_name=b'Create Datetime', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trailer',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'Is Active'),
        ),
        migrations.AddField(
            model_name='trailer',
            name='update_datetime',
            field=models.DateTimeField(verbose_name=b'Update Datetime', auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trailer',
            name='license_num',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='year',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='visitedlocation',
            name='driver',
            field=models.ForeignKey(to='trailers.Driver'),
        ),
        migrations.AddField(
            model_name='visitedlocation',
            name='location',
            field=models.ForeignKey(to='trailers.Location'),
        ),
        migrations.AddField(
            model_name='visitedlocation',
            name='trailer',
            field=models.ForeignKey(to='trailers.Trailer'),
        ),
    ]
