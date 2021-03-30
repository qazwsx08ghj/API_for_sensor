from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class IoT_sensor_info(models.Model):
    temp = models.FloatField(max_length=50, null=True, blank=True)
    humi = models.FloatField(max_length=50, null=True, blank=True)
    light = models.FloatField(max_length=50, null=True, blank=True)
    UV = models.FloatField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

