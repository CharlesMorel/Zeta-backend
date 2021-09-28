from django.db import models



class Frisbee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    pUHT=models.CharField(max_length=50)
    Range=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'frisbee'


class Process(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    step_description = models.CharField(max_length=200)
    fk_frisbee=models.ForeignKey(Frisbee, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'process'
