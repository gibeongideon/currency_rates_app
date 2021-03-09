from django import forms
from .models import GetExchangeRate


class GetExchangeRateForm(forms.ModelForm):
    class Meta:
        model = GetExchangeRate
        fields =('user','base_currency', 'target_currency', 'amount', 'rate')
        read_only_fields = ('rate')

