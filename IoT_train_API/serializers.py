from rest_framework import serializers
from .models import IoT_sensor_info


class IoT_sensor_POST_Serializer(serializers.ModelSerializer):
    user = serializers.RelatedField(read_only=True)

    class Meta:
        model = IoT_sensor_info
        fields = ['user', 'temp', 'humi', 'light', 'UV', 'moisture']

    def save(self, **kwargs):
        sensor_info = IoT_sensor_info(
            user=kwargs['user'],
            **self.validated_data
        )
        sensor_info.save()


class IoT_sensor_GET_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IoT_sensor_info
        fields = ['user', 'temp', 'humi', 'light', 'UV', 'moisture']
