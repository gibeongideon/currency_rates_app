from rest_framework import viewsets
from rest_framework import permissions
# from rest_framework import generics #, permissions, viewsets, serializers,filters, status
from .models import GetExchangeRate
from .serializer import GetExchangeRateSerializer

class GetExchangeRateViewSet(viewsets.ModelViewSet):
    """ViewSet for the ExchangeRate class"""

    permission_classes = (permissions.IsAuthenticated,)  # alow only authenticated user to access API End points

    queryset = GetExchangeRate.objects.all()#order_by('created_at')

    # def get_queryset(self):
    #     queryset = GetExchangeRate.objects.all()#filter(user_id=self.kwargs["user"])
    #     return queryset

    serializer_class = GetExchangeRateSerializer

    # search_fields = ('target_currency', )
    # ordering_fields = ('created_at', )
      