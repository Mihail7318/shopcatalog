from django import forms
from catalog.choices_str import (PRICE_CHOICES, MANUFACTURER_CHOICES, GARANTY_CHOICES, TYPE_SIZE_CHOICES,
                                 MOTHERBOARD_FORM_CHOICES)


class PriceForm(forms.Form):
    price = forms.ChoiceField(label="Цена", choices=PRICE_CHOICES, widget=forms.RadioSelect(), required=False)


class BrandForm(forms.Form):
    brand = forms.ChoiceField(label="Производитель", choices=MANUFACTURER_CHOICES,
                              widget=forms.CheckboxSelectMultiple(),
                              required=False)


class GuaranteeForm(forms.Form):
    guarantee = forms.ChoiceField(label="Гарантия", choices=GARANTY_CHOICES,
                                  widget=forms.CheckboxSelectMultiple(),
                                  required=False)


class TypesizeForm(forms.Form):
    typesize = forms.ChoiceField(label="Типоразмер", choices=TYPE_SIZE_CHOICES,
                                 widget=forms.CheckboxSelectMultiple(),
                                 required=False)


class MotherboardForm(forms.Form):
    mother = forms.ChoiceField(label="Материнская плата", choices=MOTHERBOARD_FORM_CHOICES,
                               widget=forms.CheckboxSelectMultiple,
                               required=False)
