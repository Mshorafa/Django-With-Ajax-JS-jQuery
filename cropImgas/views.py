from django.shortcuts import render
from .models import CroopImag
from django.http import JsonResponse

from .forms import CroopImagForm


# Create your views here.

def main_view(request):
    context = {}
    crop_model = CroopImag.objects.get(pk=1)
    crop_form = CroopImagForm(request.POST or None, request.FILES or None)
    if crop_form.is_valid():
        crop_form.save()
        return JsonResponse({'message': 'works'}, status=200)

    context = {
        'crop_form': crop_form,
    }
    return render(request, 'cropper/cropper.html', context)
