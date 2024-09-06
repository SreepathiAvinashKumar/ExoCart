from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from cart.models import Cart


def login_view(request):
    a = AuthenticationForm(request)    
    if len(request.POST)==0:
        return render(request,'registration/login.html',{'form':a})
    else:
        user = request.POST['username']
        password =request.POST['password']
        d=authenticate(request,username=user,password=password)
        if d is not None:
            login(request,d)
            request.session['cartcount'] =d.cart_set.all().count()
            wi = {}
            wiq = d.whishlist_set.all()
            for i in wiq:
                wi[i.product.id]=True
            request.session['wi']=wi
            # c = Cart.objects.filter(user=request.user)
            # d=0
            # for i in c :
            #  d = d+i.product.product_price  
            # request.session["cartsum"]=d 
            return redirect('shop:home')
        else:
            return render(request,'registration/login.html')    


def logout_view(request):
     logout(request)
     return redirect('shop:home')


def signup(request):
     if request.method=="POST":
      uname = request.POST['uname']
      upass = request.POST['password']
      uemail = request.POST['email']
    
         
      if uname==upass==uemail=='':
          messages.warning(request,"Please enter the given details")
          return redirect('user:signup')   
      else:
          user =User.objects.create_user(uname, uemail,upass)
          return redirect('shop:home')
     return render(request,'registration/signup.html')
     
    
