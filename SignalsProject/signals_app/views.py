from .models import *
from .serializer import *
from rest_framework import viewsets

class PurchaseViewset(viewsets.ModelViewSet):
    queryset=Purchase.objects.all()
    serializer_class=PurchaseSerializer


class StockViewset(viewsets.ModelViewSet):
    queryset=Stock.objects.all()
    serializer_class=StockSerializer