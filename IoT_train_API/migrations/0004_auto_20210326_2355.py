# Generated by Django 3.1.7 on 2021-03-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_train_API', '0003_auto_20210326_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iot_sensor_info',
            name='UV',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='iot_sensor_info',
            name='humi',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='iot_sensor_info',
            name='light',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='iot_sensor_info',
            name='temp',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
    ]