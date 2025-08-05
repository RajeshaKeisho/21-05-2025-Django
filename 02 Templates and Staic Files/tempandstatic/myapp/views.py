from django.shortcuts import render
import datetime
# Create your views here.

def wish(request):
    time = datetime.datetime.now()
    name = "ABC"
    rollno = 101
    marks = 90
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    my_dict = {'insert_date':formatted_time, "Name":name, "RollNo":rollno, "Marks":marks}
    return render(request, "wish.html", my_dict)

def wish1(request):
    time = datetime.datetime.now()
    msg = " Hello friends!! Very Very Good"
    h = int(time.strftime("%H"))
    if h<12:
        msg+=" MORNING!" 
    elif h<16:
        msg+= " AFTERNOON"
    elif h<21:
        msg+= " EVENING"
    else:
        msg = "Hello Guest, Good Night!!!"
    my_dict = {"insert_time":time, "insert_data":msg}
    return render(request, 'wish1.html', context=my_dict)

def greet(request):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if now.hour < 12:
        greeting = 'Good Morning!'
    elif now.hour < 16:
        greeting = 'Good Afternoon!'
    else:
        greeting = "Good Evening!"
    return render(request, 'greet.html', {"greeting":greeting, 'current_time':current_time})

