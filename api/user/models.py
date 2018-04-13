from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.models import EmailAddress, EmailConfirmationHMAC

class WallUser(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']

    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=False, unique=True)

    def __str__(self):
        return self.username

    def is_verified(self):
        """
        Check users related EmailAddress object
        that holds its verification info.
        """

        user_email = EmailAddress.objects.filter(user=self).first()
        is_verified = user_email.verified

        return is_verified
