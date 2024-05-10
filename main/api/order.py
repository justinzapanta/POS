from ..models import Invoice, Orders, Products
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
import json


@csrf_exempt
def new_invoice(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        today = datetime.today().strftime('%Y/%m/%d')
        count_orders = Orders.objects.values('order_number').distinct().count()
        count_invoice = Invoice.objects.values('invoice')

        for product in data['data']:
            product_instance = Products.objects.get(product_id=int(product['product_id']))
            if product_instance:
                orders = Orders(
                        order_item=product_instance,
                        order_item_total_price=int(product['product_total_price']),
                        order_number=count_orders,
                        order_date=today,
                    )
                orders.save()

        

        return JsonResponse({'message' : 'success'}, status=200)
    