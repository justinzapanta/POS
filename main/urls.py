from django.urls import path
from . import views
from .api import order

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name=('dashboard')),
    path('products/<str:category>/', views.products, name=('products')),

    #Auth
    path('login/', views.login_view, name=('login')),
    path('logout/', views.logout_view, name='logout'),

    #api
    path('api/invoice/new-invoice', order.new_invoice)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)