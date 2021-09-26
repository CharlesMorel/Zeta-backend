from django.db import models
from frisbee_model import Frisbee
from ingredient_model import Ingredient

class Frisbee_Ingredient(models.Model):
    pfk_ingredient_id=models.ForeignKey(Ingredient, related_name='ingredients', on_delete=models.CASCADE)
    pfk_frisbee_id=models.ForeignKey(Frisbee, related_name='frisbee_ref', on_delete=models.CASCADE)
    grammage=models.IntegerField()


    class Meta:
        managed = False
        db_table = 'frisbee_ingredient'