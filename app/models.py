from django.db import models
import uuid

from django.utils import timezone


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=NewsModel.Status.Draft)


class Category(models.Model):
    name = models.CharField(max_length=150, default='default_category')

    def __str__(self):
        return self.name


class NewsModel(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True)
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Status(models.TextChoices):
        Draft = "Df", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250)
    images = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)

    objects = models.Manager()

    published = PublishedManager()

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):

        return self.title