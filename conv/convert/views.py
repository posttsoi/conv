from django.shortcuts import render
from django.http import HttpResponse

from .models import ExchangeRates
from .models import convert_money
from .models import get_price

from .forms import ExchangeRatesForm


def home_page(request):
    rates = [rate.currency for rate in ExchangeRates.objects.all()]
    if request.method == 'POST':
        form = ExchangeRatesForm(request.POST)

        your_currency = request.POST.get('your_currency')  # без этого костыля форма невалидна
        desired_currency = request.POST.get('desired_currency')
        form.fields['your_currency'].choices = [(your_currency, your_currency)]
        form.fields['desired_currency'].choices = [(desired_currency, desired_currency)]

        if form.is_valid():
            your_money = form.data['your_money']
            your_currency = get_price(form.data['your_currency'])
            desired_currency = get_price(form.data['desired_currency'])

            money = convert_money(your_currency, desired_currency, your_money)
            return render(request, 'convert/index.html', context={'rates': rates, 'form': form, 'money': money})
    form = ExchangeRatesForm()
    money = ''
    return render(request, 'convert/index.html', context={'rates': rates, 'form': form, 'money': money})