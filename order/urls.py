from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
   path("", views.index, name="index"),
   path("show/<int:rid>",views.show,name="show"),
]
