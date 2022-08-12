from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def hello(request):
    kk='<h2> hi helo<h2>'
    return HttpResponse(kk)

def gm(request):
    kk='<h2> Good moring<h2>'
    return HttpResponse(kk)

def gn(request):
    kk='<h2> Good night<h2>'
    return HttpResponse(kk)
