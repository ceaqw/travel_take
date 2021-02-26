from django.db import models


# Create your models here.
class CityInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    city_name = models.CharField(max_length=50)
    head_img_url = models.CharField(max_length=50)
