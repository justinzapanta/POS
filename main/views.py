from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'main/views/index.html')

def login_view(request):
    return render(request, 'main/views/login.html')