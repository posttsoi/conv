from django.shortcuts import render
from django.http import HttpResponse

from .models import ExchangeRates


def home_page(request):
    rates = ExchangeRates.objects.all()
    return render(request, 'convert/home_page.html', context={'rates': rates})


def convert(request):
    a = request.Post
    return HttpResponse('<h1>{{a}</h1>')
