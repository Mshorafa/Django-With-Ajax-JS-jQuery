import json
from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from django.forms.models import model_to_dict

from tasks.models import DoTask


# Create your views here.


class serachView(ListView):
    model = DoTask
    template_name = "search/serach.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['qs_json'] = DoTask.objects.values()
        context['qs_json'] = json.dumps(list(DoTask.objects.values('title')))
        # return JsonResponse(model_to_dict({'context': context}), status=200)
        return context
