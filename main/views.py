from django.shortcuts import render, redirect
from .models import Products, Sales

# Create your views here.
def dashboard(request):
    return render(request, 'main/views/dashboard.html')

def products(request, category):
    categories = Products.objects.values('product_category').distinct()
    products = Products.objects.filter(product_category=str(category).title())

    data = {
            'categories' : categories,
            'products' : products,
        }


    return render(request, 'main/views/products.html', data)

def login_view(request):
    return render(request, 'main/views/login.html')