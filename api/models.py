from django.db import models


class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)

    class Meta:
        __table_name__ = "user_info"


# Create your models here.
class CityInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    city_name = models.CharField(max_length=50)
    head_img_url = models.CharField(max_length=50)

    class Meta:
        __table_name__ = "c_info"


class MomentInfo(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.CharField(max_length=50)
    like_list = models.JSONField(default=[])
    content = models.CharField(max_length=500, default='')
    user_head = models.URLField(max_length=100, default='http://xxx')
    img_url = models.URLField(max_length=100, default='http://xxx')

    class Meta:
        __table_name__ = "moment_info"
