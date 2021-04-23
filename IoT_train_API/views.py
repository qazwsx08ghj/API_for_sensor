# django modules
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

# rest_framework_API_module
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

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
    curl --location --request POST 'http://127.0.0.1:8000/api/POST_IoT_sensor_info' \
    --header 'Authorization: Basic {{b_64code}}' \
    --form 'temp="{{ sensor data }}"' \
    --form 'humi="{{ sensor data }}"'
    --form 'light="{{ sensor data }}"' \
    --form 'UV="{{ sensor data }}"'
    """


    u = User.objects.get(id=request.user.id)
    print(request.META.get('HTTP_AUTHORIZATION'))
    if request.method == "POST":
        serializer = IoT_sensor_POST_Serializer(data=request.data)
        httpResponse = {}
        if serializer.is_valid():
            serializer.save(user=u)
            httpResponse['request'] = 'success {}'.format(serializer.data)
            return Response(httpResponse)
        else:
            httpResponse['request'] = 'error'
            return Response(httpResponse)


class IoT_sensor_GET_View(RetrieveAPIView):
    """
    using curl code
    curl --location --request GET 'http://127.0.0.1:8000/api/GET_IoT_sensor_info' \
    --header 'Authorization: Basic {{b_64code}}'

    """
    serializer_class = IoT_sensor_GET_Serializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['user', 'temp', 'humi', 'light', 'UV']
    queryset = IoT_sensor_info.objects.all()
    # def get_queryset(self):
    #     u = User.objects.get(id=self.request.user.id)
    #     queryset = IoT_sensor_info.objects.all()
    #     queryset = queryset.filter(user=u)
    #     return queryset

    def get_object(self, *args, **kwargs):
        u = User.objects.get(id=self.request.user.id)

        return self.queryset.filter(user=u).latest("id")


def main_page_submit(request):
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
