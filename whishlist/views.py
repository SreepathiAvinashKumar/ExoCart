from django.shortcuts import redirect, render
from shop.models import Product
from cart.models import Cart
from .models import Whishlist
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

@login_required
def index(request):
    w = Whishlist.objects.all()
    context={
        "wl_items":w,
    }
    return render(request,"wl/index.html",context)

@login_required
def add(request,w_id):
    w = Whishlist()
    p = Product.objects.get(pk=w_id)
    w.product=p
    w.user=request.user 
    w.save()
    wi = {}
    wiq = request.user.whishlist_set.all()
    for i in wiq:
     wi[i.product.id]=True
    wi[w_id]=True
    request.session['wi']=wi
    return redirect('shop:product',w_id)
    
@login_required
def remove(request,w_id):
    w= Whishlist.objects.get(pk=w_id)
    w.delete()
    del request.session['wi']
    wi = {}
    wiq = request.user.whishlist_set.all()
    for i in wiq:
       wi[i.product.id]=True
       wi[w_id]=True
       request.session['wi']=wi

    return redirect('whishlist:index')   

