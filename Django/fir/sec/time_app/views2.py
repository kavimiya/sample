from django.shortcuts import render
from django.http import HttpResponse
import datetime




# Create your views here.


def tell(request):
    time=datetime.datetime.now()
    return HttpResponse('<h1>hi guys </h1>'+str(time))

