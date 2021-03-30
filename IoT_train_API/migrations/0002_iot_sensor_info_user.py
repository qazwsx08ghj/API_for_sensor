# Generated by Django 3.1.7 on 2021-03-26 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('IoT_train_API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iot_sensor_info',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]