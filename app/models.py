from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class Test(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, default='')
    age = models.IntegerField(default=0)
