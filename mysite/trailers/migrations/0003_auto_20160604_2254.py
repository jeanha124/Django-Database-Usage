# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trailers', '0002_auto_20160603_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitedLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.PositiveIntegerField(verbose_name=b'Visited Location Type', choices=[(0, b'start'), (1, b'transit'), (2, b'end')])),
                ('visited_datetime', models.DateTimeField(verbose_name=b'Location Visit Datetime')),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2016, 6, 5, 2, 54, 6, 653314, tzinfo=utc), verbose_name=b'Create Datetime', auto_now_add=True)),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2016, 6, 5, 2, 54, 6, 653336, tzinfo=utc), verbose_name=b'Update Datetime', auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is Active')),
                ('driver', models.OneToOneField(to='trailers.Driver')),
                ('location', models.OneToOneField(to='trailers.Location')),
                ('trailer', models.OneToOneField(to='trailers.Trailer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='driver',
            name='trailer',
        ),
        migrations.RemoveField(
            model_name='location',
            name='ending_location',
        ),
        migrations.RemoveField(
            model_name='location',
            name='location_name',
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
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 5, 2, 54, 6, 652116, tzinfo=utc), verbose_name=b'Create Datetime', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driver',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'Is Active'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driver',
            name='update_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 5, 2, 54, 6, 652140, tzinfo=utc), verbose_name=b'Update Datetime', auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='address_1',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Address 1', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='address_2',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Address 2', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name=b'City', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='create_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 5, 2, 54, 6, 652617, tzinfo=utc), verbose_name=b'Create Datetime', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'Is Active'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Location Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='phone',
            field=models.CharField(max_length=16, null=True, verbose_name=b'Phone Number', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=100, null=True, verbose_name=b'State', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='update_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 5, 2, 54, 6, 652641, tzinfo=utc), verbose_name=b'Update Datetime', auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='zipcode',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Zip Code', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trailer',
            name='create_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 5, 2, 54, 6, 651631, tzinfo=utc), verbose_name=b'Create Datetime', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trailer',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'Is Active'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trailer',
            name='update_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 5, 2, 54, 6, 651660, tzinfo=utc), verbose_name=b'Update Datetime', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trailer',
            name='trailer_index',
            field=models.CharField(unique=True, max_length=10),
            preserve_default=True,
        ),
    ]
