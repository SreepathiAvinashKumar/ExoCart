from django.urls import path
from . import views

app_name='whishlist'

urlpatterns = [
  path("",views.index,name="index"),
    path("remove/<int:w_id>",views.remove,name="remove"),
    path("add/<int:w_id>",views.add,name="add"),    
]
