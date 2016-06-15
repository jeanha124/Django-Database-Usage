from django.shortcuts import render
from django.http import HttpResponse
from .forms import VisitedLocationForm
from trailers.models import Trailer
# Create your views here.


def index(request):
    user = request.user
    TrailerFormSet = formset_factory(VisitedLocationForm)

    if request.method == 'POST':
        trailer_formset = TraielrFormSet(request.POST)

    new_trailer_locations = []

    for trailerss in trailer_formset:
        location = trailerss.cleaned_data.get('location')
        type = trailerss.cleaned_data.get('VisitedLocation')

        if location and type:
            new_trailer_locations.append(UserLink(user=user, location=location, type=type))

        try:
            with transaction.atomic():
                UserLink.object.filter(user=user).de;ete()
                UserLink.objects.bulk_create(new_trailer_locations)

                messages.succes(request, 'You have entered the trailer information')

        except IntegrityError:
            messages.error(request, 'There was an error')
            return redirect(reverse('trailer-settings'))

    else:
        trailer_formset = TrailerFormSet(initial = trailer_Data)

    context = {
        'trailer_formset': trailer_formset,
    }


    #form = VisitedLocationForm()
    #context = {
    #    "form": form,
    #}
    return render(request, 'trailers/index.html', context)

def trailer_detail(request, trailer_index):
    instance = get_object_or_404(VisitedLocation, id=id)
    context = {
        ""
    }
def trailer_list(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % trailer_index)
