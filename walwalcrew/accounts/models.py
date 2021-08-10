from django.db import models

# Create your models here.
class nickname_list(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)
    kakaoid = models.CharField(null=False,blank=False,max_length=1000)

class authentication(models.Model):
    id = models.AutoField(primary_key=True)
    authentication_id = models.ForeignKey("nickname_list", related_name="authentication_id", on_delete=models.CASCADE, db_column="authentication_id",default=False)
    authentication_date = models.DateField(auto_now_add=True, blank=False, null=False)
    authentication_email = models.CharField(max_length=100, null=False)