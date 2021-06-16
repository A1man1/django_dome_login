from django.db import models

# Create your models here.
class user_base(models.Model):
        user_name =models.CharField(max_length=25)
        name= models.CharField(max_length=30)
        phone= models.CharField(max_length=15)
        password = models.CharField(max_length=400)
