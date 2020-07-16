from django import http
from django.http import HttpResponse
from django.shortcuts import render

from catalog.choices_str import MANUFACTURER_CHOICES
from catalog.forms import BrandForm
from catalog.models import Corpus
from catalog.forms import *


# Create your views here.


def catalog(request) -> HttpResponse:
    objects = Corpus.objects.all()
    search_value = ""
    pr = ""
    if request.method == "GET":
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            search_value = q
            objects = objects.filter(name__icontains=q)

        if 'price' in request.GET and request.GET['price']:
            pr = request.GET['price']
            pricerange = pr.split('-')
            objects = objects.filter(price__gte=pricerange[0], price__lte=pricerange[1])
        if 'brand' in request.GET and request.GET['brand']:
            br = dict(request.GET)['brand']
            objects = objects.filter(manufacturer__in=br)

        if 'guarantee' in request.GET and request.GET['guarantee']:
            gr = dict(request.GET)['guarantee']
            objects = objects.filter(guarantee__in=gr)

        if 'typesize' in request.GET and request.GET['typesize']:
            tps = dict(request.GET)['typesize']
            objects = objects.filter(type_size__in=tps)
    return render(request, 'catalog.html', {'corpuses': objects,
                                            'search_value': search_value,
                                            'priceform': PriceForm({'price': pr}),
                                            'brandform': BrandForm,
                                            'guaranteeform': GuaranteeForm,
                                            'typesizeform': TypesizeForm
                                            })
