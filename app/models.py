from django.db import models

# Create your models here.

class NewsModel(models.Model):
    title = models.CharField(max_length=2000)
    images = models.ImageField()
