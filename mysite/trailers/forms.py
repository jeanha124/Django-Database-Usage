from django import forms

from .models import VisitedLocation

class VisitedLocationForm(forms.ModelForm):
    class Meta:
        model = VisitedLocation
        fields = [
        'trailer',
        'driver',
        'visited_datetime']
