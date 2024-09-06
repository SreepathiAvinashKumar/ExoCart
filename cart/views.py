from http import client
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from cart.models import Cart
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order, OrderForm, OrderItem
from django.contrib.auth.models import User
import razorpay
from django.views.decorators.csrf import csrf_exempt





@login_required
def index(request):
    c = Cart.objects.filter(user=request.user)
    d =0
    for i in c :
       d = d+i.product.product_price
    context ={
     "carts":Cart.objects.filter(user=request.user),
     "sum":d
    }
    return render(request,'index.html',context)

@login_required
def add(request,p_id):
    d =request.user.cart_set.filter(product__id=p_id)
    
    if (d.count() > 0):
        p =d[0]
        p.quantity+=1 
        p.save()
    else:    
     c = Cart()
     p = Product.objects.get(pk=p_id)
     c.user = request.user 
     c.product = p
     c.save()
     messages.success(request,"Cart Added successfully!")
     request.session['cartcount']=request.session['cartcount']+1
   #  return redirect('shop:product',p_id)
    return redirect('cart:index')

@login_required
def remove(request,c_id):
      d =Cart.objects.get(pk=c_id)
      if d.quantity > 1:
         d.quantity-=1
         d.save()
      else:
         d.delete()
      messages.warning(request,"Cart Removed Successfully!")
      request.session['cartcount']=request.session['cartcount']-1
      return redirect('cart:index')


# @login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user)
    d=0
    for i in cart:
       d = d+i.product.product_price
    if request.method =='POST': 
       t = Order(customer=request.user)
       t.status =True 
       t.price = d 
       
       fr = OrderForm(request.POST,instance=t)                
       if fr.is_valid():         
         ord = fr.save()
       for i in cart:
          o = OrderItem()
          o.product = i.product
          o.quantity = i.quantity     
          o.price   = i.product.product_price
          o.order = ord
          o.save()
       
       cart = cart.delete()
       request.session['cartcount'] =request.user.cart_set.all().count()
       wi = {}
       wiq = request.user.whishlist_set.all()
       for i in wiq:
         wi[i.product.id]=True
       request.session['wi']=wi
       
       return redirect('cart:pay')

    else: 
      fr = OrderForm()  
      context ={
         "form":fr,
               }

      return render(request,'checkout.html',context)


@csrf_exempt
def pay(request):
    global payment
    client = razorpay.Client(auth=("rzp_test_JEOWdxgp4rEZpG","gFyHs4ysnbXGvWNdixo0rjQV"))
        
    payment = client.order.create({'amount': 50000, 'currency': "INR", 'payment_capture':'0'})
    return render(request,'check.html')