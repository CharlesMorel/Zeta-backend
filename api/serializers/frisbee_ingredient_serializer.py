from api.models.frisbee_ingredient_model import PostFrisbeeIngredient
from rest_framework import serializers


class PostFrisbeeIngredientSerializer(serializers.ModelSerializer):
    Pfk_frisbee_id=serializers.PrimaryKeyRelatedField
    class Meta:
        model = PostFrisbeeIngredient
        fields = ['Pfk_frisbee_id', 'Pfk_ingredient_id', 'Grammage',]


