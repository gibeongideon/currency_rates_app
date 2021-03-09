from rest_framework import serializers
from .models import GetExchangeRate

# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token

# Use ModelSerializer to safe rates to database/ Oterwize it not nessesary because so 
# serializers.Serializer can do te trick
class GetExchangeRateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = GetExchangeRate
        # fields = ('__all__')
        fields =('created_at','base_currency', 'target_currency', 'amount', 'rate')
        read_only_fields = ('created_at','rate')
