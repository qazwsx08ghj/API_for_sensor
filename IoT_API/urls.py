"""IoT_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from IoT_train_API.views import (
    IoT_sensor_GET_View,
    IoT_sensor_POST_View,
    main_page_submit,
    main_page_get_b64
)

urlpatterns = [
    path('get_b64/', main_page_get_b64, name="get_b64"),
    path('', main_page_submit, name="main"),
    path('admin/', admin.site.urls),
    path('api/GET_IoT_sensor_info', IoT_sensor_GET_View.as_view(), name='GET_IoT_sensor_info'),
    path('api/POST_IoT_sensor_info', IoT_sensor_POST_View, name='POST_IoT_sensor_info'),
]
