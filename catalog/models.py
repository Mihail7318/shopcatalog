from django.db import models
from catalog.choices_str import *


# Create your models here.


class Corpus(models.Model):
    price = models.IntegerField(default=0)
    manufacturer = models.CharField(max_length=20, choices=manufacturer_choises)
    type_size = models.CharField(max_length=20, choices=type_size_choices)
    guarantee = models.IntegerField(default=1)
    motherboard_form = models.CharField(max_length=20, choices=motherboard_form_choices)
    psu = models.CharField(max_length=20, choices=psu_choices)
    front_window = models.BooleanField()
    gamers = models.BooleanField()
    fans_set = models.CharField(max_length=20, choices=fans_set_choices)
    illumination = models.CharField(max_length=20, choices=illumination_choices)
    color = models.CharField(max_length=20, choices=color_choices)
    integrated_psu = models.BooleanField()
    number_of_compartments = models.IntegerField(default=1)
    image = models.ImageField()
