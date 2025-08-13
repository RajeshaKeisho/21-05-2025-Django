from django.urls import path
from .views import (
    task_list_create, task_update, task_delete, TaskListCreateView, TaskUpdate, TaskDelete
)

urlpatterns = [
    path('', task_list_create, name='task_list'),
    path('update/<int:pk>', task_update, name='task_update'),
    path('delete/<int:pk>', task_delete, name='task_delete'),

    path("cbv/", TaskListCreateView.as_view(), name="cbv_task_list"),
    path("cbv/update/<int:pk>/", TaskUpdate.as_view(), name="cbv_task_update"),
    path("cbv/delete/<int:pk>/", TaskDelete.as_view(), name="cbv_task_delete"),

]