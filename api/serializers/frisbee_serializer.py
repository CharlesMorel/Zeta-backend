from api.models.frisbee_model import Frisbee, FrisbeeIngredient, Ingredient
from rest_framework import serializers




class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields = ['id','name','description']




class FrisbeeIngredientSerializer(serializers.ModelSerializer):
    ingredient=IngredientSerializer(many=True)

    class Meta:
        model=FrisbeeIngredient
        fields = ['grammage','ingredient',]
        depth = 2

class FrisbeeSerializer(serializers.ModelSerializer):
    list_ingredients=IngredientSerializer(many=True)
    class Meta:
        model=Frisbee
        fields = ['name','list_ingredients']
        depth = 1