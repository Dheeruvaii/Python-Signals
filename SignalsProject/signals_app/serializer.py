from rest_framework import serializers
from .models import *


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase
        fields='__all__'



class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields='__all__'