from django.conf import settings
from decimal import Decimal
from .exchange_api import  OpenExchange
from .mocks import response

def exc_api():

    # resp = {
    #     "disclaimer": "Exchange rates provided by [...]",
    #     "license": "Data collected and blended [...]",
    #     "timestamp": 1319730758,
    #     "base": "USD",
    #     "rates": {
    #         "AED": 4.672626,
    #         "AFN": 48.3775,
    #         "ALL": 110.223333,
    #         "AMD": 409.604993,
    #         "YER": 215.035559,
    #         "ZAR": 8.416205,
    #         "ZMK": 4954.411262,
    #         "ZWL": 322.355011,
    #         'KSH': 100.0,
    #         'USH': 1000.0,
    #         'TSH': 2000.0,
    #         'BTN': 005.0,}
    # }

    # return resp
    # resp = OpenExchange()    
  
    return response  # resp.get_rates()



def get_rates_to_usd(base_currency_name, target_currency_name):

    resp = exc_api()

    if str(base_currency_name).strip() == str(resp['base']).strip():
        base_rate_to_usd = 1
    else:
        base_rate_to_usd = resp['rates'][str(base_currency_name)]

    if str(target_currency_name).strip() == str(resp['base']).strip():
        target_rate_to_usd = 1
    else:
        target_rate_to_usd = resp['rates'][str(target_currency_name)]

        
    return base_rate_to_usd, target_rate_to_usd


def get_exchange_rate(amount,base_currency_name, target_currency_name): 
    """convert base currency to taret base on """
    base_rate_to_usd, target_rate_to_usd = get_rates_to_usd(base_currency_name, target_currency_name)
    multiplier = (float(target_rate_to_usd)/float(base_rate_to_usd)) 

    return multiplier * float(amount)



