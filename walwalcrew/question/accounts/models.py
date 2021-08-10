from django.db import models

# Create your models here.
class nickname_list(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)
