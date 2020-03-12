from django.db import models
import requests

class ExchangeRates(models.Model):
    currency = models.CharField(max_length=40, db_index=True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.currency}=={self.price}"

    def get_json_data(self):
        """get json with ExchangeRates"""
        url = 'https://openexchangerates.org/api/latest.json?app_id=d7720497b9c64663b4fe575400b66fd7'
        data = requests.get(url)
        return data.json()['rates']
