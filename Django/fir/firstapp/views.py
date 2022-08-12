from django.shortcuts import render
from django.http import HttpResponse


def love(request):
    msg='<h1> hi i love you </h1>'
    return HttpResponse(msg)

def lusu(request):
    lu='<h2> hi  welcome sathish </h2>'
    return HttpResponse(lu)

# Create your views here.



