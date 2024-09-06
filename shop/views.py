
from django.shortcuts import redirect, render
from django.http import HttpResponse

from cart.models import Cart
from .models import Product,Category
from order.models import Order
from django.http import JsonResponse
from django.core import serializers
 #from django.contrib.auth.decorators import login_required

from .models import ProductForm


def home(request):
    request.session['test']='testing'
    context ={
        
        "products":Product.objects.all(),
          
    }
    return render(request,'home.html',context)
      
def userprofile(request):
    return render(request, 'userprofile.html')



def customerservice(request):
    return render(request, 'customer_service.html')

def order(request):   
    #data = serializers.serialize('json', Cart.objects.filter(user=request.user),fields=('product__product_Name','product_price'))
    ci = Cart.objects.filter(user=request.user)
    l = []
    for p in ci:
        k={}
        k['id']=p.product.id
        k['pname']=p.product.product_Name
        k['price']=p.product.product_price
        l.append(k)

    return JsonResponse(l,safe=False)
   
def product(request,product_id):
     p = Product.objects.get(pk=product_id)
     context = {
        "productis":p
     }

     return render(request,'product.html',context)    


# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)


def search(request):
    products = Product.objects.filter(product_Name__icontains = request.GET['keyword'])
    data = request.GET['keyword']
    context ={
        "products":products,
        "keyword":products.count,
        "data":data
    }
    return render(request,'search.html',context)

def categoryview(request,cat_id):
    context ={
        
     "products":Product.objects.filter(category=cat_id)
    }
    return render(request,'categoryview.html',context)    



def sellview(request):
    fa = ProductForm()
    if request.method =='POST':
       fa = ProductForm(request.POST, request.FILES)      
       if fa.is_valid():
         print(fa.data)
         fa.save()
       return redirect('shop:home')    
    else:
      c =Category.objects.all()     
      context ={
         "category":c,
         "form":fa,
               }
      
      return  render(request,'sellproducts.html',context)


def dummy(request):
    return render(request,'keys.html')
