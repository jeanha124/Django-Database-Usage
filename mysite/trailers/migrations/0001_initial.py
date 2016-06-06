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
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Datetime')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Update Datetime')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is Active')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'Location Name', blank=True)),
                ('address_1', models.CharField(max_length=100, null=True, verbose_name=b'Address 1', blank=True)),
                ('address_2', models.CharField(max_length=100, null=True, verbose_name=b'Address 2', blank=True)),
                ('city', models.CharField(max_length=100, null=True, verbose_name=b'City', blank=True)),
                ('state', models.CharField(max_length=100, null=True, verbose_name=b'State', blank=True)),
                ('zipcode', models.CharField(max_length=15, null=True, verbose_name=b'Zip Code', blank=True)),
                ('phone', models.CharField(max_length=16, null=True, verbose_name=b'Phone Number', blank=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Datetime')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Update Datetime')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is Active')),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trailer_index', models.CharField(unique=True, max_length=10)),
                ('owner', models.CharField(max_length=10, null=True, blank=True)),
                ('vin_num', models.CharField(max_length=20, null=True, blank=True)),
                ('license_num', models.CharField(max_length=6, null=True, blank=True)),
                ('length', models.CharField(max_length=15, null=True, blank=True)),
                ('year', models.CharField(max_length=4, null=True, blank=True)),
                ('manufacturer', models.CharField(max_length=10, null=True, blank=True)),
                ('reg_date', models.CharField(max_length=8, null=True, blank=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Datetime')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Update Datetime')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is Active')),
            ],
        ),
        migrations.CreateModel(
            name='VisitedLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.PositiveIntegerField(verbose_name=b'Visited Location Type', choices=[(0, b'start'), (1, b'transit'), (2, b'end')])),
                ('visited_datetime', models.DateTimeField(verbose_name=b'Location Visit Datetime')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Datetime')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Update Datetime')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is Active')),
                ('driver', models.ForeignKey(to='trailers.Driver')),
                ('location', models.ForeignKey(to='trailers.Location')),
                ('trailer', models.ForeignKey(to='trailers.Trailer')),
            ],
        ),
    ]
