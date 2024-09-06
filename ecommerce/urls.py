from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


handler404 = 'shop.views.custom_404'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('accounts/',include('useraccounts.urls')),
    path("whishlist/",include("whishlist.urls")),
    path('cart/',include('cart.urls')),
    path('orders/',include('order.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
