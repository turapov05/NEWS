from django.db import models

# Create your models here.

class NewsModel(models.Model):
    title = models.CharField(max_length=2000)
    text = models.TextField()
    images = models.ImageField()

    def __str__(self):
        return self.title
