from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .template_view import xchange_rate

router = DefaultRouter()

app_name = 'currency_conversion_api'

router.register(r'', views.GetExchangeRateViewSet,basename='GetExchangeRate')

urlpatterns = [
    path('convert', include(router.urls)),
    # path('', xchange_rate, name="xchange_rate"),
    
]
