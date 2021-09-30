
from django.db import models


class PostFrisbeeIngredient(models.Model):
    Pfk_ingredient_id=models.IntegerField()
    Pfk_frisbee_id=models.IntegerField()
    Grammage=models.IntegerField( blank=True)
    class Meta:
        managed = False
        db_table = 'frisbee_ingredient'
        unique_together=("Pfk_ingredient_id", "Pfk_frisbee_id")

class GetFrisbeeIngredient(models.Model):
    Pfk_ingredient_id=models.IntegerField(primary_key=True)
    Pfk_frisbee_id=models.IntegerField()
    Grammage=models.IntegerField( blank=True)
    class Meta:
        managed = False
        db_table = 'frisbee_ingredient'
        unique_together=("Pfk_ingredient_id", "Pfk_frisbee_id")

