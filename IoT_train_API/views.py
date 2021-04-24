# django modules
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# rest_framework_API_module
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveAPIView

# models
from .models import IoT_sensor_info
from django.contrib.auth.models import User

# serializers
from .serializers import IoT_sensor_POST_Serializer, IoT_sensor_GET_Serializer

# base64 encode for curl
import base64

# Create your views here.


@api_view(["POST"])
def IoT_sensor_POST_View(request):
    """
    This API POST view handling the sensor trying to POST data to database and sent the success or error response to client
    , we filter the user by Basic Authorization, so we need user create first and get their own code.
    """

    httpResponse = dict()

    try:
        u = User.objects.get(id=request.user.id)
        if request.method == "POST":
            serializer = IoT_sensor_POST_Serializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user=u)
                httpResponse['request'] = 'success {}'.format(serializer.data)
                return Response(httpResponse)
            else:
                httpResponse['request'] = 'error'
                return Response(httpResponse)
    except User.DoesNotExist:
        httpResponse['request'] = 'Auth error'
        return Response(httpResponse)


class IoT_sensor_GET_View(RetrieveAPIView):
    """
    This API GET view handling the front-side GET method. Basically, when you trying to use that url like: "http://{{your GET API url}}"
    you will get json object like:
    {
        "user": 1,
        "temp": 50.0,
        "humi": 15.0,
        "light": 15.0,
        "UV": 15.0,
        "moisture": null
    }

    In front-side,if you using JavaScript, you can using that code like this:
    let get_data = (url) =>{
        return fetch(url).then(response =>
            response.json()
        ).then(json =>{
            console.log(json["data_key"]);
        })
    }

    To get an object {{in this case "json"}} that you can get data form GET method like using python dictionary object like:
    {{dict["data_key"]}}
    """

    serializer_class = IoT_sensor_GET_Serializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['user', 'temp', 'humi', 'light', 'UV']
    queryset = IoT_sensor_info.objects.all()

    def get_object(self, *args, **kwargs):
        u = User.objects.get(id=self.request.user.id)

        return self.queryset.filter(user=u).latest("id")


def main_page_submit(request):
    """
    This view handling the POST method that try to submit in this page and redirect to get b64 code page.
    In this case, I using built-in UserCreationForm that django already have it.
    """

    if request.method == "POST":
        Form = UserCreationForm(request.POST)
        if Form.is_valid():
            Form.save()
        else:
            render(request, 'submit.html', {'form': Form})
    else:
        Form = UserCreationForm(request.POST)
        context = {'form': Form}

        return render(request, 'submit.html', context)
    return redirect('/get_b64', request)


def main_page_get_b64(request):
    """
    In this view, we do a silly way to handle the Django Basic Authorization using Base 64 encoder (b64 code).
    In POST method, we need to using Basic Authorization to the check the current user, so we need to using the output in Arduino code.
    We login the user to let header can identify the user and get the user data when using the chart page.
    """
    if request.method == "POST":
        datas = {
            'b64_code': base64.b64encode(str.encode("{}:{}".format(request.POST["username"], request.POST["password"])))
        }

        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        login(request, user)
        print(request.user.is_anonymous)
        return render(request, "get_b64_page.html", datas)
    return render(request, "get_b64_page.html")


def chart(request):
    print(request.user.is_anonymous)
    return render(request, "chart.html")
