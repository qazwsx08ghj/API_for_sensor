# API_for_sensor

## how to set up 

# !!!Remember to Change your ip location in template/chart.html!!!


* Clone this project to your dictionary 


```shellscript
example:
C:\Users\NPUST\Desktop>git clone https://github.com/qazwsx08ghj/API_for_sensor.git

```

* Go into this dir with shell


```shellscript
example:
C:\Users\NPUST\Desktop>git clone https://github.com/qazwsx08ghj/API_for_sensor.git

C:\Users\NPUST\Desktop>cd API_for_sensor

C:\Users\NPUST\Desktop\API_for_sensor>

```

* Using pip command to install requirments.txt


```shellscript
example:
C:\Users\NPUST\Desktop>git clone https://github.com/qazwsx08ghj/API_for_sensor.git

C:\Users\NPUST\Desktop>cd API_for_sensor

C:\Users\NPUST\Desktop\API_for_sensor>

C:\Users\NPUST\Desktop\API_for_sensor>pip install -r requirements.txt
```

* Then run this server


```shellscript
example:
C:\Users\NPUST\Desktop>git clone https://github.com/qazwsx08ghj/API_for_sensor.git

C:\Users\NPUST\Desktop>cd API_for_sensor

C:\Users\NPUST\Desktop\API_for_sensor>

C:\Users\NPUST\Desktop\API_for_sensor>pip install -r requirements.txt -v

C:\Users\NPUST\Desktop\API_for_sensor>py manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 30, 2021 - 17:38:07
Django version 3.1.7, using settings 'IoT_API.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.

```

* POST method cUrl


```shellscript
curl --location --request POST 'http://{your_computer_IP}:8000/api/POST_IoT_sensor_info' \
    --header 'Authorization: Basic {{b_64code}}' \
    --form 'temp="{{ sensor data }}"' \
    --form 'humi="{{ sensor data }}"'
    --form 'light="{{ sensor data }}"' \
    --form 'UV="{{ sensor data }}"'
```

* GET method cUrl

``` shellscript
    curl --location --request GET 'http://{your_computer_IP}:8000/api/GET_IoT_sensor_info' \
    --header 'Authorization: Basic {{b_64code}}'
```

