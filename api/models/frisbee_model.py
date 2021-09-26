from django.db import models
from frisbee_ingredient_model import Frisbee_Ingredient

class Frisbee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    pUHT=models.CharField(max_length=50)
    Range=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'frisbee'