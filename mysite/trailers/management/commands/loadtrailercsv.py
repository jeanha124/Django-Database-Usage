import os
import csv
from django.conf import settings
from trailers.models import Trailer
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Loading CSV"
        csv_path = os.path.join(settings.BASE_DIR, "trailer_data.csv")
        with open(csv_path, 'rU') as csv_file:
            csv_reader = csv.DictReader(csv_file, dialect=csv.excel)

            for row in csv_reader:
                print(row)
                obj = Trailer.objects.create(
                    trailer_index=row['Trailer'],
                    owner=row['Owner'],
                    vin_num=row['VIN #'],
                    license_num=row['License #'],
                    length=row['Length'],
                    year=str(row['Year']),
                    manufacturer=row['Manufacturer'],
                    reg_date=row['Reg Date']
                )
                print obj
