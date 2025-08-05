from django.urls import path
from .views import morning_message, afternoon_message, evening_message

urlpatterns = [
    path('morning/', morning_message, name='morning'),
    path('noon/', afternoon_message, name='noon'),
    path('evening/', evening_message, name='evening'),
]