from django.db import models
from django.db.models.fields import DateTimeField
from cart.models import Cart
from shop.models import Product
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm
class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    # quantity =  models.IntegerField(default=1)
    price = models.IntegerField(blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    status = models.BooleanField(default=False)
    date = models.DateField(default=datetime.datetime.today)
    email =models.CharField(max_length=50)
    

class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE,null=True, blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity =  models.IntegerField(default=1)



class OrderForm(ModelForm):
     class Meta:
        model = Order
        #fields = ]
        exclude = ['customer','status','price']
    
