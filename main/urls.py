from django.urls import path
from . import views
from .api import order, inventory

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name=('dashboard')),
    path('products/<str:category>/', views.products, name=('products')),
    path('inventory/', views.inventory, name="inventory"),

    #Auth
    path('login/', views.login_view, name=('login')),
    path('logout/', views.logout_view, name='logout'),

    #api
    path('api/invoice/new-invoice/', order.new_invoice),
    path('api/inventory/get-data/', inventory.get_ingredient)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)