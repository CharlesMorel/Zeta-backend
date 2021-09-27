from api.models.frisbee_model import Frisbee, FrisbeeIngredient, Ingredient
from rest_framework import serializers




class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields = ['name','description']



class FrisbeeIngredientSerializer(serializers.ModelSerializer):

    pfk_ingredient=IngredientSerializer(read_only=True)
    class Meta:
        model = FrisbeeIngredient
        fields = ('pfk_ingredient', 'grammage')
        depth=2




class FrisbeeSerializer(serializers.ModelSerializer):
    '''To display product with related materials '''
    list_ingredients = serializers.SerializerMethodField()

    class Meta:
        model = Frisbee
        fields = ('name', 'list_ingredients')
        depth=2
    def get_list_ingredients(self, frisbee_instance):
        query_datas = FrisbeeIngredient.objects.filter(pfk_frisbee=frisbee_instance)
        return [FrisbeeIngredientSerializer(ingredient).data for ingredient in query_datas]