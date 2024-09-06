from django.shortcuts import render
from order.models import Order,OrderItem



def index(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request,'od/index.html',context={'orders':orders})

def show(request, rid):
    e = OrderItem.objects.filter(order__id=rid)
    return render(request,'od/show.html',context={'oitems':e})


