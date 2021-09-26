from django.db import models

class Ingredient(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'ingredient'




class Frisbee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    pUHT=models.CharField(max_length=50)
    Range=models.IntegerField()
    list_ingredients=models.ManyToManyField(Ingredient, related_name='ingredient', through="FrisbeeIngredient", through_fields=("pfk_frisbee","pfk_ingredient"))


    class Meta:
        managed = False
        db_table = 'frisbee'

class FrisbeeIngredient(models.Model):
    pfk_ingredient=models.OneToOneField(Ingredient, on_delete=models.CASCADE,related_name='ingredients')
    pfk_frisbee=models.OneToOneField(Frisbee, on_delete=models.CASCADE,related_name='frisbees')
    grammage=models.IntegerField()


    class Meta:
        managed = False
        db_table = 'frisbee_ingredient'
        unique_together=("pfk_ingredient_id", "pfk_frisbee_id")







