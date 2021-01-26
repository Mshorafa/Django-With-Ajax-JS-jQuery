from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import DropZone


# Create your views here.


class main(TemplateView):
    model = DropZone
    template_name = "dropzone/DropZone.html"


def fileUploud(request):
    if request.FILES:
        if request.method == 'POST':
            my_imgae = request.FILES.get('file')
            DropZone.objects.create(file=my_imgae)
            return HttpResponse('')
    return JsonResponse({'POST': 'False'})
