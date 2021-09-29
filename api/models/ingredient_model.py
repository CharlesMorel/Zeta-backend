from django.db import models

class Ingredient(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'ingredient'


class Frisbee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    pUHT=models.CharField(max_length=50)
    Range=models.IntegerField()
    list_ingredients=models.ManyToManyField(Ingredient, through="FrisbeeIngredient", through_fields=("pfk_frisbee","pfk_ingredient"), )


    class Meta:
        managed = False
        db_table = 'frisbee'

class FrisbeeIngredient(models.Model):
    pfk_ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ref_ingr")
    pfk_frisbee=models.OneToOneField(Frisbee, on_delete=models.CASCADE, primary_key=True,  unique=False)
    grammage=models.IntegerField( blank=True)


    class Meta:
        managed = False
        db_table = 'frisbee_ingredient'
        unique_together=("pfk_ingredient", "pfk_frisbee")



