from django import http
from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Corpus
from catalog import forms


# Create your views here.


def catalog(request) -> HttpResponse:
    objects = Corpus.objects.all()
    search_value = ""
    pr = ""
    if request.method == "GET":
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            search_value = q
            objects = objects.filter(name__icontains=search_value)
        if 'pr' in request.GET and request.GET['pr']:
            pr = request.GET['pr']
            pricerange = pr.split('-')
            objects = objects.filter(price__gte=pricerange[0], price__lte=pricerange[1])

    return render(request, 'catalog.html', {'corpuses': objects,
                                            'search_value': search_value,
                                            'priceform': forms.RadioPriceForm({'pr': pr}),
                                            })
