from django.contrib import admin
from .models import Currency, ExchangeRate


class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'code', 'name',)
    list_display_links = ('id',)


admin.site.register(Currency, CurrencyAdmin)


class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = (
        'id','created_at', 'base_currency', 'target_currency', 'rate',)
    list_display_links = ('id',)

admin.site.register(ExchangeRate, ExchangeRateAdmin)


