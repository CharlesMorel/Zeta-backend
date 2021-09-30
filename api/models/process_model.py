from django.db import models



class Frisbee(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    PUHT=models.CharField(max_length=50)
    Range=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'frisbee'


class GetProcess(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    StepDescription = models.CharField(max_length=200, db_column='step_description')
    Frisbee=models.ForeignKey(Frisbee, on_delete=models.CASCADE, db_column='fk_frisbee_id')
    class Meta:
        managed = False
        db_table = 'process'

class PostProcess(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    StepDescription = models.CharField(max_length=200, db_column='step_description')
    FrisbeeId=models.ForeignKey(Frisbee, on_delete=models.CASCADE, db_column='fk_frisbee_id')
    class Meta:
        managed = False
        db_table = 'process'