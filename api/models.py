from django.db import models


class LoginTrial(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    try_at = models.DateTimeField()
    success = models.BooleanField(default=False)
