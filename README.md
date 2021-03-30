# API_for_sensor

## how to set up 


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

C:\Users\NPUST\Desktop\API_for_sensor>py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 30, 2021 - 17:38:07
Django version 3.1.7, using settings 'IoT_API.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```

* POST method cUrl


```shellscript
curl --location --request POST 'http://127.0.0.1:8000/api/POST_IoT_sensor_info' \
    --header 'Authorization: Basic {{b_64code}}' \
    --form 'temp="{{ sensor data }}"' \
    --form 'humi="{{ sensor data }}"'
    --form 'light="{{ sensor data }}"' \
    --form 'UV="{{ sensor data }}"'
```

* GET method cUrl

``` shellscript
using curl code
    curl --location --request GET 'http://127.0.0.1:8000/api/GET_IoT_sensor_info' \
    --header 'Authorization: Basic {{b_64code}}'
```

