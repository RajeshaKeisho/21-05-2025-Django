from django.urls import path
from .views import display, greeting

urlpatterns = [
    path('display/', display, name='display'),
    path('greeting/', greeting, name='greeting'),
]