from django.urls import path
from . import views

app_name='task'

urlpatterns=[
    path('',views.TaskList.as_view(),name='TaskListUrl'),
    path('<int:id>/completed/',views.CompletedTask.as_view(),name='Completed_Task'),
    path('<int:id>/removeTask/',views.removeTask.as_view(),name='Remove_Task'),
]