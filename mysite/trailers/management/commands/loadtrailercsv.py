import os
import csv
from django.conf import settings
from trailers.models import Trailer
from django.core.management.base import BaseCommand

class Command(BaseCommand):

	def handle(self, *args, **options):
		print "Loading CSV"
		csv_path = os.path.join(settings.BASE_DIR, "trailer_data.csv")
		csv_file = open(csv_path, 'rb')
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			obj = Trailer.objects.create(
				trailer_index=['Trailer'],
				owner=['Owner'],
				vin_num=['Vin #'],
				license_num=['License #'],
				length=['Length'],
				year=['Year'],
				manufacturer=['Manufacturer'],
				reg_date=['Reg Date']
			)
			print obj
