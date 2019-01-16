from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "Product"

