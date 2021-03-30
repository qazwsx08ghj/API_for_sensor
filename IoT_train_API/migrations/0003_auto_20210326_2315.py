# Generated by Django 3.1.7 on 2021-03-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_train_API', '0002_iot_sensor_info_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iot_sensor_info',
            name='UV',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iot_sensor_info',
            name='humi',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iot_sensor_info',
            name='light',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iot_sensor_info',
            name='temp',
            field=models.FloatField(max_length=50),
        ),
    ]
