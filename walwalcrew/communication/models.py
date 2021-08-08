from django.db import models

# Create your models here.
class question_list(models.Model):
    id = models.AutoField(primary_key=True)
    cateogry = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=5000)
    answer = models.CharField(max_length=5)
    date = models.DateField(auto_now_add=True, blank=True, null=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey("question_list", related_name="question_id", on_delete=models.CASCADE, db_column="question_id")
    text = models.CharField(max_length=5000,null=False)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    nickname = models.CharField(max_length=100, null=True)
    like = models.BigIntegerField(blank=False,null=True,default=0)
    unlike = models.BigIntegerField(blank=False,null=True,default=0)