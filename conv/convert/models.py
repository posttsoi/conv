from django.db import models
import requests


def get_json_data():
    """get json with exchange rates"""
    url = 'https://openexchangerates.org/api/latest.json?app_id=d7720497b9c64663b4fe575400b66fd7'
    data = requests.get(url)
    return data.json()['rates']


def update_data() -> None:
    """cleans bd and adds new data"""
    data_exchange_rate = get_json_data()
    ExchangeRates.objects.all().delete()
    for currency, price in data_exchange_rate.items():
        ExchangeRates.objects.create(currency=f'{currency}', price=price)


class ExchangeRates(models.Model):
    currency = models.CharField(max_length=20, db_index=True)
    price = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self) -> str:
        return f"{self.currency}=={self.price}"
