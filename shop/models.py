from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models import fields
from django.db.models.deletion import CASCADE
from django.forms import ModelForm, Textarea





class Category(models.Model):
      category_name = models.CharField(max_length=200)
      
      @staticmethod
      def get_all_categories():
        return Category.objects.all()

      def __str__(self):
        return self.category_name    
  

# class Customer(models.Model):
#     first_Name = models.CharField(max_length=100)
#     second_Name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.IntegerField(default=0)
#     password = models.CharField(max_length=20)


#     def register(self):
#         self.save()

#     @staticmethod
#     def get_customer_by_email(email):
#         try:
#             return Customer.objects.get(email=email) 
#         except:
#             return False

#     def is_Exists(self):
#         if Customer.objects.filter(email=self.email):
#             return True
#         else :
#             return False
                
#     def __str__(self):
#         return self.first_Name+self.second_Name


class Product(models.Model):
    
    product_Name = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='',blank=True)
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/',default='')
    image3 = models.ImageField(upload_to='products/',default='')
    image4 = models.ImageField(upload_to='products/',default='')
    # image5 = models.ImageField(upload_to='products/',default='')
    # image6 = models.ImageField(upload_to='products/',default='')
    tags = models.CharField(max_length=400,null=True)

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_prodcts():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)        
        else :
            return Product.get_all_prodcts()


    def __str__(self):
        return self.product_Name  






class ProductForm(ModelForm):
    
    class Meta:
        model=Product        
        exclude = ['category']
        widgets = {
            'description': Textarea(attrs={'cols': 90, 'rows': 80}),
        }
        

          