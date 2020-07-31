from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Corpus
from catalog.forms import *


# Create your views here.


def catalog(request) -> HttpResponse:
    objects = Corpus.objects.all()
    search_value = ""

    if request.method == "GET":
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            search_value = q
            objects = objects.filter(name__icontains=q)

        if 'price' in request.GET and request.GET['price']:
            price = request.GET['price']
            pricerange = price.split('-')
            objects = objects.filter(price__gte=pricerange[0], price__lte=pricerange[1])

        if 'brand' in request.GET and request.GET['brand']:
            brand = dict(request.GET)['brand']
            objects = objects.filter(manufacturer__in=brand)

        if 'guarantee' in request.GET and request.GET['guarantee']:
            guarantee = dict(request.GET)['guarantee']
            objects = objects.filter(guarantee__in=guarantee)

        if 'typesize' in request.GET and request.GET['typesize']:
            typesize = dict(request.GET)['typesize']
            objects = objects.filter(type_size__in=typesize)

        if 'mother' in request.GET and request.GET['mother']:
            mother = dict(request.GET)['mother']
            objects = objects.filter(motherboard_form__in=mother)

        if 'psu' in request.GET and request.GET['psu']:
            psu = dict(request.GET)['psu']
            objects = objects.filter(psu__in=psu)

        if 'fans' in request.GET and request.GET['fans']:
            fans = dict(request.GET)['fans']
            objects = objects.filter(fans_set__in=fans)

        if 'illumination' in request.GET and request.GET['illumination']:
            illumination = dict(request.GET)['illumination']
            objects = objects.filter(illumination__in=illumination)

        if 'color' in request.GET and request.GET['color']:
            color = dict(request.GET)['color']
            objects = objects.filter(color__in=color)

        if 'gamers' in request.GET and request.GET['gamers']:
            gamers = dict(request.GET)['gamers'][0]
            objects = objects.filter(gamers=gamers)

        if 'compartments' in request.GET and request.GET['compartments']:
            compartments = int(dict(request.GET)['compartments'][0])
            objects = objects.filter(number_of_compartments=compartments)
    init_data = {"price": "",
                 "brand": "",
                 "type_size": "",
                 "mother": "",
                 "psu": "",
                 "fans": "",
                 "illumination": "",
                 "color": ""
                 }
    filter_form = FilterForm(request.GET, initial=init_data)
    return render(request, 'catalog.html', {'corpuses': objects,
                                            'search_value': search_value,
                                            'FilterForm': filter_form,
                                            })
