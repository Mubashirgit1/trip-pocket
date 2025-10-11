from django.shortcuts import render
from django.http import HttpResponse


def my_trip(request):
    return render(request, "blog/index.html")
# Create your views here.
