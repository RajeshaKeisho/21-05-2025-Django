# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils import timezone
import datetime

def display(request):
    s = "<h1> Hello, Students! Welcome to Django Class</h1>"
    return HttpResponse(s)

def greeting(request):
    current_time = timezone.now()
    hour = current_time.hour

    if 6 <= hour < 12:
        greeting_message = "Good Morning!"
    elif 12 <= hour < 16:
        greeting_message = "Good Afternoon!"
    else:
        greeting_message = "Good Evening!"

    formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"{greeting_message}! Today, the date and time is: {formatted_time}")




