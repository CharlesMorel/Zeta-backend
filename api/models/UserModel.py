from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    uid = models.CharField(max_length=254)
    cn = models.CharField(max_length=254)
    sn = models.CharField(max_length=254)
    givenName = models.CharField(max_length=254)
    userPassword = models.CharField(max_length=254)
    mail = models.EmailField(max_length=254)


def create_user_profile(sender, instance, created, **kwargs):
    UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)