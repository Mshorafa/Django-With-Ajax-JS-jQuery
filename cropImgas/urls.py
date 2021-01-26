from django.urls import path

from . import views

app_name = 'cropImgas'

urlpatterns = [
    path('', views.main_view, name='main-view')
]
