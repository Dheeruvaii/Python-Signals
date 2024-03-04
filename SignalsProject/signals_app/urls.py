from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'stock', StockViewset, basename='Stock-Itemlists')
router.register(r'purchase', PurchaseViewset, basename='Purchase-Itemlists')




urlpatterns = [
    path('/', include('router.urls')),
]
