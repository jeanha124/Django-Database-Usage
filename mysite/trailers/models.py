from django.db import models

# Create your models here.

class Trailer (models.Model):
	trailer_index = models.CharField(max_length=10, unique=True)
	owner = models.CharField(max_length=10, blank=True, null=True)
	vin_num = models.CharField(max_length=20, blank=True, null=True)
	license_num = models.CharField(max_length=6, blank=True, null=True)
	length = models.CharField(max_length=15, blank=True, null=True)
	year = models.IntegerField(blank=True, null=True)
	manufacturer = models.CharField(max_length=10, blank=True, null=True)
	reg_date = models.CharField(max_length=8, blank=True, null=True)

	def __str__(self):
		return self.trailer_index

class Driver (models.Model):
	first_name = models.CharField(max_length=20)
	trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name
class Location (models.Model):
	location_name = models.CharField(max_length=50)
	starting_location = models.CharField(max_length=50)
	transit_location = models.CharField(max_length=50, blank=True, null=True)
	ending_location = models.CharField(max_length=50)
	trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
	
	def __str(self):
		return self.location_name
