
from django.db import models


class PostFrisbeeIngredient(models.Model):
    pfk_ingredient_id=models.IntegerField()
    pfk_frisbee_id=models.IntegerField()
    grammage=models.IntegerField( blank=True)
    class Meta:
        managed = False
        db_table = 'frisbee_ingredient'
        unique_together=("pfk_ingredient_id", "pfk_frisbee_id")

class GetFrisbeeIngredient(models.Model):
    pfk_ingredient_id=models.IntegerField(primary_key=True)
    pfk_frisbee_id=models.IntegerField()
    grammage=models.IntegerField( blank=True)
    class Meta:
        managed = False
        db_table = 'frisbee_ingredient'
        unique_together=("pfk_ingredient_id", "pfk_frisbee_id")

