from beer.models import Brewery, Beer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response


def brewery(request, brewery_id):
    b = get_object_or_404(Brewery, pk=brewery_id)
    return render_to_response('beer/brewery.html', {'brewery': b})

def beer(request, beer_id):
    b = get_object_or_404(Beer, pk=beer_id)
    return render_to_response('beer/beer.html', {'beer': b})
