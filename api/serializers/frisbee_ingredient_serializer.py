from api.models.frisbee_ingredient_model import PostFrisbeeIngredient
from rest_framework import serializers


class PostFrisbeeIngredientSerializer(serializers.ModelSerializer):
    pfk_frisbee_id=serializers.PrimaryKeyRelatedField
    class Meta:
        model = PostFrisbeeIngredient
        fields = ['pfk_frisbee_id', 'pfk_ingredient_id', 'grammage',]


