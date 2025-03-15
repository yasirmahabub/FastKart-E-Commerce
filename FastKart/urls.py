from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('products.urls')),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
]
