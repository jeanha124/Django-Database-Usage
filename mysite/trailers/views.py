from django.shortcuts import render
from django.http import HttpResponse
from .forms import VisitedLocationForm
from trailers.models import Trailer
# Create your views here.


def trailer_location_create(request):
    form = VisitedLocationForm()
    context = {
        "form": form,
    }
    return render(request, 'trailers/index.html', context)

def trailer_detail(request, trailer_index):
    instance = get_object_or_404(VisitedLocation, id=id)
    context = {
        ""
    }
def trailer_list(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % trailer_index)
