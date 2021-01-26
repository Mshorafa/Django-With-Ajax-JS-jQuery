from django.urls import path
from . import views

app_name = 'dropz'
urlpatterns = [
    path('', views.main.as_view(), name='drop-zone'),
    path('upload/', views.fileUploud, name='fileUploud'),

]
