from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Ingredients
import json

@csrf_exempt
def update_ingredient(request):
    data = json.loads(request.body)
    if data:
        ingredient = Ingredients.objects.get(ingredient_id=data['id'])
        exist = Ingredients.objects.filter(ingredient_expiration_date=data['new_date'], ingredient_name=data['new_name'])

        if not exist or data['date'] == data['new_date']:
            ingredient.ingredient_name = data['new_name']
            ingredient.ingredient_quantity = data['quantity']
            ingredient.ingredient_unit = data['unit']
            ingredient.ingredient_expiration_date = data['new_date']
            ingredient.save()
            return JsonResponse({'message' : 'success'}, status=200)
        else:
            exist[0].ingredient_quantity = (exist[0].ingredient_quantity + ingredient.ingredient_quantity)
            exist[0].save()

            ingredient.delete()
    return JsonResponse({'message' : 'Error'}, status=200)

    