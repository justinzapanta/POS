from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import Ingredients
import json

@csrf_exempt
def get_ingredient(request):
    data = json.loads(request.body)

    ingredient = Ingredients.objects.filter(ingredient_name=data['ingredient_name'])
    ingredient_list = []
    for gredient in ingredient:
        ingredient_list.append({
                'ingredient_quantity' : gredient.ingredient_quantity,
                'unit' : gredient.ingredient_unit,
                'expiration_date' : gredient.ingredient_expiration_date,
                'ingredient_id' : gredient.ingredient_id
            }
         )
    
    return JsonResponse({ 'ingredient_list' : ingredient_list}, status=200)