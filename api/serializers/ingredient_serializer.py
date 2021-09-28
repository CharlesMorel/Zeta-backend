from api.models.ingredient_model import Frisbee, FrisbeeIngredient, Ingredient
from rest_framework import serializers
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields = ['id','name','description']





