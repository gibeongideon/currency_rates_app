from django.conf import settings
import json
from .models import Currency, ExchangeRate
from .exceptions import RateFetchException, RateSaveException
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import logging
logger = logging.getLogger(__name__)

class OpenExchange(object):

    def __init__(self):
        """ Initialize wit url setup/create/build"""
        # https://openexchangerates.org/api/latest.json?app_id=25c609e398224b8a88050704fc3ec0f0&base=USD
        self.url = f"{settings.OPENEXCHANGE_URL}?app_id={settings.OPENEXCHANGE_APP_ID}&base={settings.BASE_CURRENCY}"


    def get_rates(self):
        """
        Return a dictionary that maps currency code with its rate value relative to basa currency 
        """
        try:
            data = urlopen(self.url).read().decode("utf-8")
            return json.loads(data)#['rates']

        except Exception as e:
            logger.exception(f"Error fetching data from {self.url}" )
            raise RateFetchException(f"Error fetching rates:{e}")
  

    def save_rates(self):
        """
        Creates rates  and save the exchange rates
        into a database  for future reference
        """ 
        fetch_rates = self.get_rates()['rates']

        for currency, value in fetch_rates.items():
            try:
                currency, _ = Currency.objects.get_or_create(name=currency)
                base_currency, _ = Currency.objects.get_or_create(
                    name=settings.BASE_CURRENCY)
                ExchangeRate.objects.create(base_currency=base_currency, target_currency=currency, rate=value)
            except Exception as e:
                raise RateSaveException(f"Error saving rates:{e}")
                pass ###
