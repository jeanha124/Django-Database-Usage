from django import forms

from .models import VisitedLocation

class VisitedLocationForm(forms.ModelForm):
    class Meta:
        model = VisitedLocation
        fields = [
        'trailer',
        'driver',
        'location', 'location_types.0',
        'location' , 'location_types.1',
        'location', 'location_types.2',
        'visited_datetime']		
