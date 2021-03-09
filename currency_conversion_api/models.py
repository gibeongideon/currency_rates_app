from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from .exceptions import InvalidAmountException


def get_exchange_rate():# avoid circular imports error

    from .conversion import  get_exchange_rate
    return get_exchange_rate

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    # is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Currency(models.Model):
    """Model holds a currency information"""
    code = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return f'{self.name}'


class ExchangeRate(TimeStamp):
    
    """Model to store exchange rates between currencies"""

    base_currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='rates', blank=True, null=True)
    target_currency = models.ForeignKey('Currency', on_delete=models.CASCADE,)
    rate = models.DecimalField(max_digits=17, decimal_places=8, blank=True, null=True)
 
    def __str__(self):
        return f'{self.base_currency} to {self.target_currency}rate is {self.rate}'



# No need to ave below model if user rates queryies need not be stored in db/
class GetExchangeRate(TimeStamp):    
    """Model to anable user to query exchange rates between currencies and store this rates in db"""  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    base_currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='queryrates')
    target_currency = models.ForeignKey('Currency', on_delete=models.CASCADE,)
    amount = models.DecimalField(max_digits=15, decimal_places=7)
    rate = models.DecimalField(max_digits=15, decimal_places=8, blank=True, null=True)
 
    def __str__(self):
        return f'{self.amount} of {self.base_currency} to {self.target_currency}'


    def get_rate(self,exchange_rate):
        try:
            rate =exchange_rate()(self.amount,self.base_currency, self.target_currency)
            return rate
        except Exception as e:
            print(e) 
            return None  

    # @property 
    def conveted_amount(self):
        return self.get_rate(get_exchange_rate)


    def save(self, *args, **kwargs):
        """Overrride internal model save method to update rate before save."""
        if self.amount < 0:
            # raise InvalidAmountException('Amount cant be negative')
            return

            # return # prevent converting neative values

        if self.base_currency.id == self.target_currency.id:
            self.rate= self.amount
        else:
            try:
                self.rate= self.conveted_amount()                
            except Exception as re:
                self.rate = 88 # rep wit None
                print(re)
                pass    
                    
        super(GetExchangeRate, self).save(*args, **kwargs)              
