from django.shortcuts import render
from django.http import HttpResponse

# view takes requests, returns response
"""respose: http, json"""
# Create your views here.

def hello_world_view(request):
    return HttpResponse("Hello World!")

