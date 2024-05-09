from django.shortcuts import render, redirect

# Create your views here.
def dashboard(request):
    return render(request, 'main/views/dashboard.html')

def products(request):
    return render(request, 'main/views/products.html')

def login_view(request):
    return render(request, 'main/views/login.html')