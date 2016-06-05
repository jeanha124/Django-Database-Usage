from django.db import models
from django.utils import timezone

# Create your models here.
class Trailer(models.Model):
	trailer_index = models.CharField(max_length=10, unique=True)
	owner = models.CharField(max_length=10, blank=True, null=True)
	vin_num = models.CharField(max_length=20, blank=True, null=True)
	license_num = models.CharField(max_length=6, blank=True, null=True)
	length = models.CharField(max_length=15, blank=True, null=True)
	year = models.IntegerField(blank=True, null=True)
	manufacturer = models.CharField(max_length=10, blank=True, null=True)
	reg_date = models.CharField(max_length=8, blank=True, null=True)

	# House-keeping
	create_datetime = models.DateTimeField('Create Datetime', default=timezone.now(), auto_now_add=True)
	update_datetime = models.DateTimeField('Update Datetime', default=timezone.now(), auto_now=True)
	is_active = models.BooleanField('Is Active', default=True)

	def __str__(self):
		return self.trailer_index


class Driver(models.Model):
	first_name = models.CharField(max_length=20)

	# House-keeping
	create_datetime = models.DateTimeField('Create Datetime', default=timezone.now(), auto_now_add=True)
	update_datetime = models.DateTimeField('Update Datetime', default=timezone.now(), auto_now=True)
	is_active = models.BooleanField('Is Active', default=True)

	def __str__(self):
		return self.first_name


class Location(models.Model):
	name = models.CharField('Location Name', blank=True, null=True, max_length=50)
	address_1 = models.CharField('Address 1', blank=True, null=True, max_length=100)
	address_2 = models.CharField('Address 2', blank=True, null=True, max_length=100)
	city = models.CharField('City', blank=True, null=True, max_length=100)
	state = models.CharField('State', blank=True, null=True, max_length=100)
	zipcode = models.CharField('Zip Code', blank=True, null=True, max_length=15)
	phone = models.CharField('Phone Number', blank=True, null=True, max_length=16)

	# House-keeping
	create_datetime = models.DateTimeField('Create Datetime', default=timezone.now(), auto_now_add=True)
	update_datetime = models.DateTimeField('Update Datetime', default=timezone.now(), auto_now=True)
	is_active = models.BooleanField('Is Active', default=True)

	def __str__(self):
		return self.name


class VisitedLocation(models.Model):
	START = 0
	TRANSIT = 1
	END = 2

	location_types = (
		(START, 'start'),
		(TRANSIT, 'transit'),
		(END, 'end')
	)

	location = models.OneToOneField(Location)
	driver = models.OneToOneField(Driver)
	type = models.PositiveIntegerField('Visited Location Type', choices=location_types)
	trailer = models.OneToOneField(Trailer)
	visited_datetime = models.DateTimeField('Location Visit Datetime')

	# House-keeping
	create_datetime = models.DateTimeField('Create Datetime', default=timezone.now(), auto_now_add=True)
	update_datetime = models.DateTimeField('Update Datetime', default=timezone.now(), auto_now=True)
	is_active = models.BooleanField('Is Active', default=True)

	def __str__(self):
		return "{location} - {trailer}".format(location=self.location.name, trailer=self.trailer.trailer_index)
