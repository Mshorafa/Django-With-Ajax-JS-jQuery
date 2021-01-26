from django.shortcuts import render
from django.http import JsonResponse

from cars.models import Car
from models.models import Model
from orders.models import Order


# Create your views here.
def main_view(request):
    qs_cars = Car.objects.all()
    context = {
        'qs_cars': qs_cars
    }
    return render(request, 'orders/main.html', context)


def get_jsoncar_data(request):
    car_val = list(Car.objects.values())
    return JsonResponse({'data': car_val}, status=200)


def get_selected_car(request, *args, **kwargs):
    select_car = kwargs.get('car')
    obj_model = list(Model.objects.filter(car__name=select_car).values())
    print(obj_model)
    return JsonResponse({'obj_model': obj_model}, status=200)


def create_Order(request):
    if request.is_ajax():
        aCar = request.POST.get('car')
        car_obj = Car.objects.get(name=aCar)
        amodel = request.POST.get('model')
        model_obj = Model.objects.get(name=amodel)
        Order.objects.create(car=car_obj, model=model_obj)
        return JsonResponse({'created': True})
    return JsonResponse({'created': False})
