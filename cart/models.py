from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


class Cart(models.Model):
      user =  models.ForeignKey(User,on_delete=models.CASCADE)
      product = models.ForeignKey(Product,on_delete=models.CASCADE)
      quantity = models.IntegerField(default=1)
      def __str__(self):
          return self.product.product_Name


