# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
def morning_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime('%d-%m-%Y %H:%M:%S')
    return HttpResponse("<h1>Hello, Good Morning! Now the time is " + formatted_time + "</h1>")

def afternoon_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime('%d-%m-%Y %H:%M:%S')
    return HttpResponse("<h1>Hello, Good Afternoon! Now the time is " + formatted_time + "</h1>")

def evening_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime('%d-%m-%Y %H:%M:%S')
    return HttpResponse("<h1>Hello, Good Evening! Now the time is " + formatted_time + "</h1>")