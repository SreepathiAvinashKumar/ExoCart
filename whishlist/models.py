from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


class Whishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    whish = models.BooleanField(default=False)  
    def __str__(self):
          return self.product.product_Name