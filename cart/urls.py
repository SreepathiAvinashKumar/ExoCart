from unicodedata import name
from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
      path("",views.index,name="index"),
      path("add/<int:p_id>",views.add,name="add"),
      path("remove/<int:c_id>",views.remove,name="remove"),
      path("checkout",views.checkout,name="checkout"),
      path("pay",views.pay,name="pay"),
    
]
