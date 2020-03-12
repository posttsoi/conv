from django.shortcuts import render
from django.http import HttpResponse

from .models import ExchangeRates


def home_page(request):
    data = ExchangeRates.objects.all()
    return render(request, 'convert/home_page.html', context={'data': data})
