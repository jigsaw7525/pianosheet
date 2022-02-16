from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Profile(AbstractUser):
    nickename = models.CharField(null=True, blank=True, max_length=150)
    certification = models.BooleanField(default=False)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return f'{self.username}'
