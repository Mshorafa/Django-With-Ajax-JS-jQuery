from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.main_view, name='orders'),
    path('json-data/', views.get_jsoncar_data, name='json-data'),
    path('select-car/<str:car>/', views.get_selected_car, name='select-car'),
    path('create-Order/', views.create_Order, name='create-Order'),
]
