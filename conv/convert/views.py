from django.shortcuts import render
from django.http import HttpResponse

from .models import ExchangeRates
from .models import convert_money
from .models import get_price

from .forms import ExchangeRatesForm


def home_page(request):
    form = ExchangeRatesForm()
    rates = ExchangeRates.objects.all()
    if request.method == 'GET':
        money = 0
        return render(request, 'convert/index.html', context={'rates': rates, 'form': form, 'money': money})
    elif request.method == 'POST':
        data = request.POST.dict()
        money = convert_money(get_price(data['your_currency']), get_price(data['desired_currency']), data['your_money'])
        return render(request, 'convert/index.html', context={'rates': rates, 'form': form, 'money': money})


