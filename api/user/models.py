from django.contrib.auth.models import AbstractUser
from django.db import models

class WallUser(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']

    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=False, unique=True)

    def __str__(self):
        return self.username
