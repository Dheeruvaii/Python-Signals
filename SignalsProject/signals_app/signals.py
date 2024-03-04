from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Stock, Purchase
 
@receiver(post_save, sender =Purchase)
def update_stock(sender, instance, **kwargs):    
    stock=Stock.objects.get(available_item = instance.item)
    stock.available_quantity = stock.available_quantity - instance.quantity
    stock.save()