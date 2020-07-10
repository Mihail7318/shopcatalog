from django import http
from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Corpus

# Create your views here.
from shop import settings


def catalog(request) -> HttpResponse:
    objects = Corpus.objects.all()
    search_value = ""
    if request.method == "GET":
        if 'q' in request.GET and request.GET['q']:
            search_value = request.GET['q']
            q = request.GET['q']
            objects = Corpus.objects.filter(name__icontains=q)
    return render(request, 'catalog.html', {'corpuses': objects, 'search_value': search_value})
