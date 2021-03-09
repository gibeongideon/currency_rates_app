from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import template_view

router = DefaultRouter()

app_name = 'currency_conversion_api'

router.register(r'', views.GetExchangeRateViewSet,basename='GetExchangeRate')

urlpatterns = [
    path('', template_view.index, name="index"),
    path('exchange_rate', include(router.urls)),
    # path('', xchange_rate, name="xchange_rate"),
    
]
