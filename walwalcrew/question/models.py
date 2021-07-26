from django.db import models

# Create your models here.
class question(models.Model):
    cateogry = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    answer = models.CharField(max_length=5)