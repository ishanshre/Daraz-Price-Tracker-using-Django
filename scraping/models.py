from django.db import models
from .utils import get_detail
import asyncio
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=512, blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_current_price = models.FloatField(default=0)
    current_price_difference = models.FloatField(default=0)
    original_price = models.FloatField(default=0)
    seller = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-created']
    
    def save(self, *args, **kwargs):
        product = get_detail(self.url)
        old_current_price = self.current_price
        if self.current_price:
            if product["current_price"] != old_current_price:
                diff = product["current_price"] - old_current_price
                self.current_price_difference = round(diff, 2)
                self.old_current_price = old_current_price

        else:
            self.old_current_price = 0
            self.current_price_difference = 0
        self.name = product['title']
        self.current_price = product['current_price']
        self.original_price = product['original_price']
        self.seller = product['seller']
        super().save(*args, **kwargs)