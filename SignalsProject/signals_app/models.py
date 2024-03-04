from django.db import models



fruits ={
    ('Apple','Apple'),
    ('Mango','Mango'),
    ('Banana','Banana'),
    ('Orange','Orange')
}

class Purchase(models.Model):
    name=models.CharField(max_length=30,choices=fruits)
    quantity =models.CharField(max_length=30)


    def __str__(self):
        return self.name
    

class Meta:
    verbose_name ="Purchase"


class Stock(models.Model):
    available_item = models.CharField(max_length=10, choices=fruits)
    available_quantity = models.IntegerField()
 
    def __str__(self):
        return self.available_item
 
    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
