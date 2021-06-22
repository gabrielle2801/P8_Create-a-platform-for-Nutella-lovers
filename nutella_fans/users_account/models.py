from django.db import models
from django.contrib.auth.models import AbstractUser
from save_substitute.models import Substitute
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):

    email = models.EmailField(
        max_length=258, verbose_name='email address', unique=True)
    password = models.CharField(max_length=128, verbose_name='password')
    substitutes = models.ManyToManyField(Substitute)

    def __str__(self):
        return self.email
