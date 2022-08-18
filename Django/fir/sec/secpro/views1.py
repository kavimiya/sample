from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.


def hello(request):
    kk='<h2> hi helo<h2>'
    return HttpResponse(kk)

def gm(request):
    kk='<h2> Good morning<h2>'
    return HttpResponse(kk)

def gn(request):
    kk='<h2> Good night<h2>'
    return HttpResponse(kk)

def telltime(request):
    time=datetime.datetime.now()
    return HttpResponse('<h1> hi guys </h1>'+str(time))
