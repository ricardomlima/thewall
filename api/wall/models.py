from django.db import models

from user.models import WallUser


# Create your models here.
class Post(models.Model):

    author = models.ForeignKey(WallUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published', auto_now_add=True)
