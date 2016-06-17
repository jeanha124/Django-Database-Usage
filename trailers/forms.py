from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from .models import VisitedLocation

class VisitedLocationForm(forms.Form):
        trailer = forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'placeholder':
        'Trailer Number',}), required=True)
        driver = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Driver', }), required=True)
        location = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Location', }), required=False)

#user_choices = [(0, 'Start'), (1, 'Transit'), (2, 'End')]
#VisitedLocationtypeFormSet = modelformset_factory(VisitedLocation, form=VisitedLocationForm)
#my_formset = VisitedLocationFormSet(self.request.POST or None)
#for choice_form in my_formset:
#    choice_form.fields['model'].choices = user_choices
      # fields = [
       #'trailer',
       #'driver',
       #'location',
       #'comments',
       #'visited_datetime']

#VisitedLocationForm() = modelformset_factory(VisitedLocation)
#formset = VisitedLocationFormSet()
#print(formset)
