from django.db import models
from django.utils import timezone
class Article(models.Model):
    artice_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.artice_name

class Author(models.Model):
    def __str__(self):
        return self.first

    first = models.CharField(max_length=500)
    last = models.CharField(max_length=500)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

# Create your models here.
