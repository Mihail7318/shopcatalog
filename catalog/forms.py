from django import forms
from static.data_src.choices_str import *


class FilterForm(forms.Form):

    price = forms.ChoiceField(label="Цена", choices=PRICE_CHOICES, widget=forms.RadioSelect(), required=False)

    brand = forms.ChoiceField(label="Производитель", choices=MANUFACTURER_CHOICES,
                              widget=forms.CheckboxSelectMultiple(),
                              required=False)

    guarantee = forms.ChoiceField(label="Гарантия", choices=GARANTY_CHOICES,
                                  widget=forms.CheckboxSelectMultiple(),
                                  required=False)
    type_size = forms.ChoiceField(label="Типоразмер", choices=TYPE_SIZE_CHOICES,
                                  widget=forms.CheckboxSelectMultiple(),
                                  required=False)

    mother = forms.ChoiceField(label="Материнская плата", choices=MOTHERBOARD_FORM_CHOICES,
                               widget=forms.CheckboxSelectMultiple,
                               required=False)

    psu = forms.ChoiceField(label="Расположение БП", choices=PSU_CHOICES,
                            widget=forms.CheckboxSelectMultiple,
                            required=False)

    fans = forms.ChoiceField(label="Кулеры", choices=FANS_SET_CHOICES,
                             widget=forms.CheckboxSelectMultiple,
                             required=False)

    illumination = forms.ChoiceField(label="Кулеры", choices=ILLUMINATION_CHOICES,
                                     widget=forms.CheckboxSelectMultiple,
                                     required=False)

    color = forms.ChoiceField(label="Цвет", choices=COLOR_CHOICES,
                              widget=forms.CheckboxSelectMultiple,
                              required=False)

    gamers = forms.ChoiceField(label="Для геймеров", choices=GAMERS_CHOICES,
                               widget=forms.CheckboxSelectMultiple, required=False)

    compartments = forms.CharField(label="Количество отсеков", required=False)
