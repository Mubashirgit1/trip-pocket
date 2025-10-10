from django.shortcuts import render
from django.http import HttpResponse
def my_trip(request):
    return HttpResponse("Hello, trip!")
# Create your views here.
