from django.db import models
 
# Create your models here. 
fruits ={
    ('Apple','Apple'),
    ('Mango','Mango'),
    ('Banana','Banana'),
    ('Orange','Orange')
}
 
class Purchase(models.Model):
    item = models.CharField(max_length=10, choices=fruits)
    quantity = models.IntegerField()
 
    def __str__(self):
        return self.item
 
    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'


class Stock(models.Model):
    available_item = models.CharField(max_length=10, choices=fruits)
    available_quantity = models.IntegerField()
 
    def __str__(self):
        return self.available_item
 
    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
