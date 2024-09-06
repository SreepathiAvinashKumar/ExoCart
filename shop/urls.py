from django.urls import path
from . import views

app_name = 'shop'

urlpatterns =[  
    path('dummy',views.dummy,name='dummy'),
    path('',views.home,name="home"),
    path("order",views.order,name="order"),
    path("product/<int:product_id>",views.product,name="product"),
    path("search",views.search,name="search"),
    path("category/<int:cat_id>",views.categoryview,name="categoryview"),
    path("sell",views.sellview,name="sell"),
    path("userprofile",views.userprofile, name="userprofile"),
     path("customerservice",views.customerservice, name="customerservice"),
  
    
]

