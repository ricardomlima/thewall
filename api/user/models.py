from django.contrib.auth.models import AbstractUser
from django.db import models

class WallUser(AbstractUser):

    USERNAME_FIELD = 'email'

    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.username
