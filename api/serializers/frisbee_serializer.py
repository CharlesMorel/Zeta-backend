from api.models.frisbee_model import Frisbee, FrisbeeIngredient, Ingredient
from rest_framework import serializers



class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields = ['Id','Name','Description']



class FrisbeeIngredientSerializer(serializers.ModelSerializer):

    Ingredient=IngredientSerializer()
    class Meta:
        model = FrisbeeIngredient
        fields = ('Ingredient', 'Grammage')
        depth=2




class GetFrisbeeSerializer(serializers.ModelSerializer):
    '''To display product with related materials '''
    ListIngredients = serializers.SerializerMethodField()

    class Meta:
        model = Frisbee
        fields = ('Id', 'Name', 'Description', 'PUHT', 'Range', 'ListIngredients')
        depth=2

    def get_ListIngredients(self, frisbee_instance):
        query_datas = FrisbeeIngredient.objects.filter(Frisbee=frisbee_instance)
        return [FrisbeeIngredientSerializer(ingredient).data for ingredient in query_datas]



class PostFrisbeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frisbee
        fields = ('Id', 'Name', 'Description', 'PUHT', 'Range')
