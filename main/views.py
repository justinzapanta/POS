from django.shortcuts import render, redirect
from .models import Orders, Invoice, Products, Ingredients
from django.db.models import Sum, Subquery, OuterRef
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        total_product_sold = Orders.objects.values('order_id').count()
        total_orders = Orders.objects.values('order_number').distinct().count()
        total_sale = Invoice.objects.all()
        
        total = 0
        for sale in total_sale:
            if sale:
                total += sale.invoice_total_price

        data = {
            'total_orders' : total_orders,
            'total_product_sold' : total_product_sold,
            'total_sale' : total
        }
        return render(request, 'main/views/dashboard.html', data)
    return redirect('login')

def products(request, category):
    if request.user.is_authenticated:
        categories = Products.objects.values('product_category').distinct()
        products = Products.objects.filter(product_category=str(category).title())

        data = {
                'categories' : categories,
                'products' : products,
            }
        return render(request, 'main/views/products.html', data)
    return redirect('login')


def login_view(request):
    data = {}
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
            )
        
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            data['notif'] = 'Invalid Username or Password'

    return render(request, 'main/views/login.html', data)

def logout_view(request):
    logout(request)
    return redirect('login')


def inventory(request):
    name_list = Ingredients.objects.values_list('ingredient_name', flat=True).order_by('ingredient_name').distinct()

    ingredients_list = []
    pagination_num = 1
    for num, name in enumerate(name_list):
        ingredients = Ingredients.objects.filter(ingredient_name=name).annotate(total_quantity=Sum('ingredient_quantity'))
        ingredients_list.append({
                'ingredient_name' : ingredients[0].ingredient_name,
                'ingredient_total_quantity' : ingredients[0].total_quantity,
                'ingredient_unit' : ingredients[0].ingredient_unit,
                'pagination_num' : pagination_num
            })
        
        if ((num + 1) % 10 ) == 0:
            pagination_num += 1
        print(pagination_num, num)

    return render(request, 'main/views/inventory.html', { 'ingredients' : ingredients_list})