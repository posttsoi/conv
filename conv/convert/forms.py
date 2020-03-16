from django import forms
from .models import ExchangeRates


class ExchangeRatesForm(forms.Form):
    your_currency = forms.ChoiceField()
    desired_currency = forms.ChoiceField()
    your_money = forms.DecimalField(error_messages={'required': '!'}, required=True)

