from django.contrib import admin
from trailers.models import Trailer, Driver, Location, VisitedLocation
# Register your models here.

@admin.register(VisitedLocation)
class VisitedLocationAdmin(admin.ModelAdmin):

    list_display = ('location', 'driver', 'type', 'trailer', 'visited_datetime', 'create_datetime', 'is_active')
    list_filter = ('is_active', 'driver__first_name', 'type', 'trailer__trailer_index', 'location__name')
    readonly_fields = ('create_datetime', )
    search_fields = ('driver__first_name', 'type', 'trailer__trailer_index', 'location__name')

admin.site.register(Trailer)
admin.site.register(Driver)
admin.site.register(Location)
