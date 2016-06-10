from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Trailer(models.Model):
	trailer_index = models.CharField(max_length=10, unique=True)
	owner = models.CharField(max_length=10, blank=True, null=True)
	vin_num = models.CharField(max_length=20, blank=True, null=True)
	license_num = models.CharField(max_length=50, blank=True, null=True)
	length = models.CharField(max_length=15, blank=True, null=True)
	year = models.CharField(max_length=4, blank=True, null=True)
	manufacturer = models.CharField(max_length=10, blank=True, null=True)
	reg_date = models.CharField(max_length=8, blank=True, null=True)

	# House-keeping
	create_datetime = models.DateTimeField('Create Datetime', auto_now_add=True)
	update_datetime = models.DateTimeField('Update Datetime', auto_now=True)
	is_active = models.BooleanField('Is Active', default=True)

	def __str__(self):
		return self.trailer_index


class Driver(models.Model):
	first_name = models.CharField(max_length=20)

	# House-keeping
	create_datetime = models.DateTimeField('Create Datetime', auto_now_add=True)
	update_datetime = models.DateTimeField('Update Datetime', auto_now=True)
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
	create_datetime = models.DateTimeField('Create Datetime', auto_now_add=True)
	update_datetime = models.DateTimeField('Update Datetime', auto_now=True)
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

	trailer = models.ForeignKey(Trailer)
	driver = models.ForeignKey(Driver)
	location = models.ForeignKey(Location)
	type = models.PositiveIntegerField('Visited Location Type', choices=location_types)
	visited_datetime = models.DateTimeField('Location Visit Datetime')

	# House-keeping
	create_datetime = models.DateTimeField('Create Datetime', auto_now_add=True)
	update_datetime = models.DateTimeField('Update Datetime', auto_now=True)
	is_active = models.BooleanField('Is Active', default=True)

	def __str__(self):
		return "{type} - {trailer} - {location}".format(
			location=self.location.name,
			trailer=self.trailer.trailer_index,
			type=dict(self.location_types).get(self.type)
		)

	class VisitedLocationForm(models.Model):
		class Meta:
			model = VisitedLocation
			fields = ['trailer', 'driver', 'location', 'location_types.0', 'location' , 'location_types.1', 'location', 'location_types.2', 'visited_datetime']		
