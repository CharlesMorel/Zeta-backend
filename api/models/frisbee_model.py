from django.db import models

class Ingredient(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'ingredient'


class Frisbee(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    PUHT=models.CharField(max_length=50)
    Range=models.IntegerField()
    ListIngredients=models.ManyToManyField(Ingredient, through="FrisbeeIngredient", through_fields=("Frisbee","Ingredient"), )


    class Meta:
        managed = False
        db_table = 'frisbee'

class FrisbeeIngredient(models.Model):
    Ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ref_ingr", db_column='pfk_ingredient_id')
    Frisbee=models.OneToOneField(Frisbee, on_delete=models.CASCADE, primary_key=True,  unique=False,db_column='pfk_frisbee_id')
    Grammage=models.IntegerField( blank=True)


    class Meta:
        managed = False
        db_table = 'Frisbee_ingredient'
        unique_together=("Ingredient", "Frisbee")



class Process(models.Model):
    Id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Step_description = models.CharField(max_length=200)
    Fk_frisbee=models.ForeignKey(Frisbee, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'process'



