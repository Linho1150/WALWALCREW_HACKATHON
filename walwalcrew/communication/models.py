from django.db import models

# Create your models here.
class question_list(models.Model):
    id = models.AutoField(primary_key=True)
    cateogry = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    answer = models.CharField(max_length=5)