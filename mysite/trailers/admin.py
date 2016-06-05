from django.contrib import admin
from trailers.models import Trailer, Driver, Location, VisitedLocation
# Register your models here.

admin.site.register(Trailer)
admin.site.register(Driver)
admin.site.register(Location)
admin.site.register(VisitedLocation)
