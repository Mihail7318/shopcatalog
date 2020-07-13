from django import forms
from catalog.choices_str import PRICE_CHOICES


class RadioPriceForm(forms.Form):
    pr = forms.ChoiceField(label="Цена", choices=PRICE_CHOICES, widget=forms.RadioSelect(), required=False)
