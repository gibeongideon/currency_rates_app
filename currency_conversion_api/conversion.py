from django.conf import settings
from decimal import Decimal
from .exchange_api import  OpenExchange


def exc_api():
    resp = OpenExchange()    
  
    return  resp.get_rates() #response#



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



