from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Corpus


# Create your views here.
from shop import settings


def catalog(request) -> HttpResponse:
    lolerball = Corpus.objects.all()
    return render(request, 'catalog.html', {'many': lolerball})
