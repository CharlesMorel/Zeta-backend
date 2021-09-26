from django.db import models

class Ingredient(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ingredient'