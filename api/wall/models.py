from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published', auto_now_add=True)
