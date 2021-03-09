from django.test import TestCase
from .models import Currency, GetExchangeRate

# Models Level Tests
class SaveCorrectModel(TestCase):

    def test_can_save_model(self):
        base_currency = Currency.objects.create(name='USD', code='840')
        target_currency = Currency.objects.create(name='KES', code='454')

        GetExchangeRate.objects.create(
            amount=100,
            base_currency=base_currency,
            target_currency= target_currency )

        self.assertEqual(GetExchangeRate.objects.count(),1)    

    def test_same_curency_base_and_target(self):
        base_currency = Currency.objects.create(name='USD', code='840')
 
        GetExchangeRate.objects.create(
            amount=100,
            base_currency=base_currency,
            target_currency= base_currency )

        self.assertEqual(float(GetExchangeRate.objects.get(id=1).rate), 100.0)

        
        GetExchangeRate.objects.create(
            amount=9999999,
            base_currency=base_currency,
            target_currency= base_currency )

        self.assertEqual(GetExchangeRate.objects.get(id=2).rate, 9999999)

    def test_correct_conveted_amount_from_base_currency(self):
        base_currency = Currency.objects.create(name='USD', code='840')
        target_currency_1 = Currency.objects.create(name='KES', code='454')
        target_currency_2 = Currency.objects.create(name='UGX', code='562')
 
        GetExchangeRate.objects.create(
            amount=1,
            base_currency=base_currency,
            target_currency= target_currency_1 )

        self.assertEqual(float(GetExchangeRate.objects.get(id=1).rate), 109.7)


        GetExchangeRate.objects.create(
            amount=1,
            base_currency=base_currency,
            target_currency= target_currency_2 )

        self.assertEqual(float(GetExchangeRate.objects.get(id=2).rate), 3663.53115300)

    def test_correct_conveted_amount_from_non_base_currency(self):
        base_currency = Currency.objects.create(name='KES', code='254')
        target_currency_1 = Currency.objects.create(name='TZS', code='654')
        target_currency_2 = Currency.objects.create(name='UGX', code='562')
 
        GetExchangeRate.objects.create(
            amount=1,
            base_currency=base_currency,
            target_currency= target_currency_1 )

        self.assertEqual(float(GetExchangeRate.objects.get(id=1).rate), 21.14842374)


        GetExchangeRate.objects.create(
            amount=1,
            base_currency=base_currency,
            target_currency= target_currency_2 )

        self.assertEqual(float(GetExchangeRate.objects.get(id=2).rate), 33.39590841)

    def test_correct_conveted_amount_from_non_base_to_base_currency(self):
        base_currency_1 = Currency.objects.create(name='KES', code='254')
        base_currency_2 = Currency.objects.create(name='UGX', code='985')
        target_currency = Currency.objects.create(name='USD', code='654')

 
        GetExchangeRate.objects.create(
            amount=1,
            base_currency=base_currency_1,
            target_currency= target_currency)

        self.assertEqual(float(GetExchangeRate.objects.get(id=1).rate), 0.00911577)


        GetExchangeRate.objects.create(
            amount=1,
            base_currency=base_currency_2,
            target_currency= target_currency )

        self.assertEqual(float(GetExchangeRate.objects.get(id=2).rate), 0.00027296)


# Test Functions



class FunctionTestCase(TestCase):
    def test_get_rates(self):
        pass

    def test_rates_are_saved(self):
        pass

