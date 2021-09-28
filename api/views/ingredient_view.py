from api.models.ingredient_model import Ingredient
from api.serializers.ingredient_serializer import IngredientSerializer
from rest_framework import generics



class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class=IngredientSerializer



class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class=IngredientSerializer