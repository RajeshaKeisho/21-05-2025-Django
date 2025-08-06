from django.urls import path
from . import views

urlpatterns = [
    path("data/", views.employee_view, name='employee')
]